def conversion_rate(date):

    from google.cloud import bigquery
    import numpy as np
    
    client = bigquery.Client()

    date = date.replace("-","")

    # Check the input date variable
    if not date.isnumeric():
        raise ValueError ("The date should be in the format YYYYMMDD")
    
    # Download query results.
    query_string = """
    SELECT fullvisitorId
         , visitId
         , date
         , visitNumber
         , device.deviceCategory
         , hits.transaction.transactionId
         , totals.visits
      FROM `bigquery-public-data.google_analytics_sample.ga_sessions_{}`
      , UNNEST (hits) hits;      
    """.format(date)

    user_story_df = (
    client.query(query_string)
    .result()
    .to_dataframe(
        # Optionally, explicitly request to use the BigQuery Storage API. As of
        # google-cloud-bigquery version 1.26.0 and above, the BigQuery Storage
        # API is used by default.
        create_bqstorage_client=True,
        )
    )

    # Fetch only rows where the visit of each user equals to One
    user_story_df = user_story_df[user_story_df['visits'] == 1] 
    # Create a new column named UserType according to the number of visits of user.    
    user_story_df['UserType'] = np.where(user_story_df['visitNumber'] == 1,'New','Returning')
    # Create a new column named SessionsStr which concatenates 3 existing columns to one in order to create a unique key of a session
    user_story_df['SessionStr'] = user_story_df['fullvisitorId'] + str(user_story_df['visitId']) + user_story_df['date']
    
    # Grouping By UserType and deviceCategory and Count Distinct Sessions and transactions
    us_grouped_df = user_story_df.groupby(['UserType', 'deviceCategory']).agg({'SessionStr':['nunique'],'transactionId':['nunique']})
    # Flatten a hierarchical index in columns
    us_grouped_df.columns = ["_".join(col).strip() for col in us_grouped_df.columns.values]
    # After grouping reset the indexing of the dataframe and rename the columns based on our needs.
    us_grouped_df = us_grouped_df.reset_index().rename(columns={"deviceCategory":"Platform","SessionStr_nunique": "Sessions", "transactionId_nunique": "Transactions"})
    # Calculating the ecommerce Conversion Rate (Calculation Formula)
    us_grouped_df['ConversionRate'] = round(us_grouped_df['Transactions']/us_grouped_df['Sessions']*100,2)
    # Print the results
    print(us_grouped_df.loc[:,['UserType', 'Platform','ConversionRate']])

    
if __name__ == "__main__":
    date = '20170101'
    conversion_rate(date)

