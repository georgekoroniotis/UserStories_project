from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = ("""
    SELECT fullVisitorId 
       FROM `bigquery-public-data.google_analytics_sample.ga_sessions_20170101` LIMIT 10""")
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.fullVisitorId)

