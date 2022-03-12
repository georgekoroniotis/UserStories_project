def user_list():

    from google.cloud import bigquery

    client = bigquery.Client()

    # Perform a query.
    QUERY = ("""
        WITH users AS (
       SELECT fullVisitorId
            , visitStartTime 
            , IFNULL(totals.timeOnSite,0) AS timeOnSite
            , ROW_NUMBER() OVER(PARTITION BY fullVisitorId ORDER BY date ASC) AS rn
       FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*` 
       WHERE visitNumber = 1
       )
    SELECT fullVisitorId as User
         , visitStartTime AS `timestamp`
         , timeOnSite AS timeToConvert  
    FROM users WHERE rn = 1

            """)
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    print('User       | Timestamp  | TimeToConvert ')
    print('----------------------------------------')
    for row in rows:
        User = row['User']
        Timestamp = row['timestamp']
        TimeToConvert = row['timeToConvert']
        print(f'{User:<20} | {Timestamp:<20} | {TimeToConvert:>4,}')
               

if __name__ == "__main__":
    user_list()
    

