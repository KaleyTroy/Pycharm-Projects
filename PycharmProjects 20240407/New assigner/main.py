import smtplib
import requests
from bs4 import BeautifulSoup

URL = "https://bunnings.service-now.com/incident_list.do?sysparm_orderby=opened&sysparm_exclude_column=parent&sysparm_exclude_column=category&sysparm_exclude_column=business_service&sysparm_order_direction=desc&sysparm_query=numberIN"
URL2 = "https://bunnings.service-now.com/incident_list.do?sysparm_query=sys_created_onONToday@javascript:gs.beginningOfToday()@javascript:gs.endOfToday()"
URL3 = 'https://bunnings.sharepoint.com/sites/ITCCTeam/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FITCCTeam%2FShared%20Documents%2F2%2E%20Shift%2DNight%20Team%20Important%20Updates%2Fdistro%2Etxt&parent=%2Fsites%2FITCCTeam%2FShared%20Documents%2F2%2E%20Shift%2DNight%20Team%20Important%20Updates'

response = requests.get(url=URL3)
soup = BeautifulSoup(response.text, 'html.parser').getText()

print(soup)


