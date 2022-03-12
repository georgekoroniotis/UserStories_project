def conversion_rate(date):

    from google.cloud import bigquery

    client = bigquery.Client()

    date = date.replace("-","")

    if not date.isnumeric():
        raise ValueError ("The date should be in the format YYYYMMDD")
    
    # Perform a query.
    QUERY = ("""
        SELECT
            UserType,
            Platform,
            ROUND(transactions/sessions*100,2) AS eCom_conversion_rate,
        FROM (
            SELECT
                CASE WHEN visitNumber = 1 THEN 'New' ELSE 'Returning' END AS UserType,
                device.deviceCategory AS Platform,
                COUNT(DISTINCT CONCAT(fullvisitorId, CAST(visitId AS string), date)) AS sessions,
                COUNT(DISTINCT hits.transaction.transactionId) AS transactions
            FROM
                `bigquery-public-data.google_analytics_sample.ga_sessions_{}`,
            UNNEST (hits) hits
            WHERE 1=1
                AND totals.visits = 1
            GROUP BY 
                CASE WHEN visitNumber = 1 THEN 'New' ELSE 'Returning' END,
                device.deviceCategory
            )
            """.format(date))
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    print('UserType   | Platform   | ConversionRate')
    print('----------------------------------------')
    for row in rows:
        UserType = row['UserType']
        Platform = row['Platform']
        ConversionRate = row['eCom_conversion_rate']
        print(f'{UserType:<10} | {Platform:<10} | {ConversionRate:>4,}')
               

if __name__ == "__main__":
    date = '20170101'
    conversion_rate(date)

