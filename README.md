# UserStories_project
Reporting some metrics of the data in the Big Query tables.

The scope of this projects by using the sample dataset, which contains obfuscated Google Analytics 360 data from the Google Merchandise Store is:
* To create a program that calculates the ecommerce Conversion Rate for a given day. The result set should be the User Type (New or Returning user) and the Platform (Desktop, Web, Mobile, Tablet).
* To create a program that fetches all users with the timestamp of their first session and their time to convert.

Two programs have been implemented for the first calculation:
- user_story_01_sql.py (SQL calculation)
- user_story_01_python.py (Python calculation utilizing Pandas library)
while
One program has been implemented for the second calculation:
-user_story_02.py (SQL implementation)

For the implementation process:
1. Create or use an existing project in the Google Cloud Platform. e.g. My first Project
2. Go to Google Cloud Shell Editor (https://cloud.google.com/shell)
3. Create a new folder 
4. Get started writing code!

![image](https://user-images.githubusercontent.com/97738060/158053750-fd71c0c3-e408-48b3-839e-a325ad09e9c1.png)
<br>

In order to test my editor, I created a .py file named app.py with the following code:

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

For the scope of the first program, I utilized Pandas library so I had to install the package first:
```cmd
pip3 install pandas
```
![image](https://user-images.githubusercontent.com/97738060/158054070-4f0fedb4-d726-4f5d-ba0a-b59a1bed2803.png)


<h3>Source Controlling </h3>

In Github, I created a new project named UserStories_project.

Initiate Git in Google Cloud Platform:<br>
![image](https://user-images.githubusercontent.com/97738060/158016772-c227be21-8d96-4a4b-8a72-04216feec6ab.png)

Connect Remote Repository: (GitHub) <br>
![image](https://user-images.githubusercontent.com/97738060/158027309-22a89f9d-c968-4e69-bd65-a8913e44104c.png)

Git Push: <br>
![image](https://user-images.githubusercontent.com/97738060/158027351-022b43c2-7410-47c1-8a0b-e0260b639f8e.png)

PrintScrreen of Running Program 1 (User Story 1):<br>
![image](https://user-images.githubusercontent.com/97738060/158017307-113d4bea-95bf-46b6-8066-37ad11d3ab8f.png)


<h3>Sources</h3>
Table Schema (https://support.google.com/analytics/answer/3437719?hl=en)<br>
eCommerce Calculation Rate (https://www.meliorum.com.au/blog/matching-big-query-data-with-google-analytics-acquisition-channel-report)<br>
GoogleAPIs BigQueries (https://github.com/googleapis/python-bigquery/tree/35627d145a41d57768f19d4392ef235928e00f72)<br>
Cloud Shell (https://cloud.google.com/shell)<br>
