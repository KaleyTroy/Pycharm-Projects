import requests

url = 'https://bunnings.service-now.com/api/now/table/incident'
username = '360593'
password = 'GOTmilk2'

params = {'sysparm_limit': 10, 'sysparm_query': 'active=true'}

response = requests.get(url, auth=(username, password), params=params)

incidents = response.json()
for incident in incidents['result']: print(incident)

