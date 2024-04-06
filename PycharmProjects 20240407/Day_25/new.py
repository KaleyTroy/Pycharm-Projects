import requests
import csv

# set the API endpoint and the required headers
endpoint = 'https://<instance>.service-now.com/api/now/table/<table_name>'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Basic <auth_token>'
}

# set the query parameters
params = {
    'sysparm_query': '<query>',
    'sysparm_fields': '<field1>,<field2>,...'
}

# send a GET request to the API endpoint
response = requests.get(endpoint, headers=headers, params=params)

# check the status code of the response
if response.status_code == 200:
    # retrieve the list of records
    records = response.json()['result']

    # open a CSV file for writing
    with open('records.csv', 'w', newline='') as f:
        # create a CSV writer
        writer = csv.DictWriter(f, fieldnames=['field1', 'field2', ...])

        # write the header row
        writer.writeheader()

        # write