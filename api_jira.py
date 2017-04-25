from jira import JIRA
from http.client import HTTPSConnection
from base64 import b64encode
import urllib.request
import requests
import json
from requests.auth import HTTPBasicAuth

class Sprints:


    def get_current_sprints(self):

      """
         Get data of maintainance team        
      """
      
      res = requests.get('https://crm.monumetric.com/rest/greenhopper/1.0/xboard/work/allData.json?rapidViewId=7&_=1493093083336', data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('rinku', 'R8ik,9ol.'))
      issues = res.json()['issuesData']['issues']
      issues_len = issues.__len__()
     
      for index in range(issues_len):
         print("id:",issues[index].get('id', "Not Assigned"))
         print("Key:",issues[index].get('key', "Not Assigned"))
         print("assignee:",issues[index].get('assignee', "Not Assigned"))
         print("assigneeName:",issues[index].get('assigneeName', "Not Assigned"))
         print("priorityName:",issues[index].get('priorityName', "Not Assigned"))
         print("done:",issues[index].get('done', "Not Assigned"))
         print("estimateStatistic:",issues[index].get('estimateStatistic', "Not Assigned"))
         print("statusId:",issues[index].get('statusId', "Not Assigned"))
         print("statusName:",issues[index].get('statusName', "Not Assigned"))
         print("status:",issues[index].get('status', "Not Assigned"),"\n\n")
         
            
obj=Sprints()
obj.get_current_sprints()
