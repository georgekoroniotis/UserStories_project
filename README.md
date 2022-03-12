# UserStories_project
Reporting some metrics of the data in the Big Query tables.

Using Pycharm IDE, I created a new project named UserStories_project.

Next, using the terminal I created a new virtual environment, activated it and continued with the installation of google-cloud-bigquery packages as follow:

```
pip install virtualenv
virtualenv BigQueryEnv
BigQueryEnv\Scripts\activate
BigQueryEnv\Scripts\pip.exe install google-cloud-bigquery
```

Next, upgrade pip if need be,

```
BigQueryEnv\Scripts\python.exe -m pip install --upgrade pip
```

In order to test my new virtual environment, I created a .py file named test.py with the following code:

```python
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.name)
```

if the run failed and the error message is the following:
> ImportError: cannot import name 'bigquery' from 'google.cloud' (unknown location)

then upgrade google packages:

```
pip install --upgrade google-cloud
pip install --upgrade google-cloud-bigquery
pip install --upgrade google-cloud-storage
```
source: https://stackoverflow.com/questions/60894798/importerror-cannot-import-name-bigquery


Connect GitHub with the Google Cloud Platform repositories (Create a mirrored repository):
1. Clicked Add repository.
2. Selected Connect external repository and clicked Continue
3. In the Project drop-down list, I selected the Google Cloud project to which the mirrored repository belongs. 
4. In the Git provider drop-down list, I selected GitHub
5. 

source: https://cloud.google.com/source-repositories/docs/mirroring-a-github-repository


How to calculate conversion rate:
-- https://support.google.com/google-ads/answer/2684489?hl=en

Initiate Git in Google Cloud Platform:
![image](https://user-images.githubusercontent.com/97738060/158016772-c227be21-8d96-4a4b-8a72-04216feec6ab.png)

PrintScrreen of Running Program 1 (User Story 1):

![image](https://user-images.githubusercontent.com/97738060/158017307-113d4bea-95bf-46b6-8066-37ad11d3ab8f.png)

<h3>Sources</h3>
Table Schema (https://support.google.com/analytics/answer/3437719?hl=en)
eCommerce Calculation Rate (https://www.meliorum.com.au/blog/matching-big-query-data-with-google-analytics-acquisition-channel-report)
GoogleAPIs BigQueries (https://github.com/googleapis/python-bigquery/tree/35627d145a41d57768f19d4392ef235928e00f72)



