from jira import JIRA
#from http.client import HTTPSConnection
#from base64 import b64encode
#import urllib.request
import requests
import json
import csv
from requests.auth import HTTPBasicAuth

class Sprints:

    

    def get_current_sprints(self):

      """
         Get Team-Board data.        
      """
      
      res = requests.get('https://crm.monumetric.com/rest/greenhopper/1.0/xboard/work/allData.json?rapidViewId=7&_=1493093083336', data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('rinku', 'R8ik,9ol.'))
      issues = res.json()['issuesData']['issues']
      issues_len = issues.__len__()
      self.create_csv('temp.csv',issues)
      
      
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
         print("status:",issues[index].get('status', "Not Assigned"))
         print("status:",issues[index]['status']['description'])
         
         print("estimateStatistic:",issues[index]['estimateStatistic']['statFieldValue'].get('value',"Not Assigned"),"\n\n")

    def create_csv(self,filename,issues):
        """
         Creating csv file of the data.
        """
        issues_l = issues.__len__()
        with open(filename,'w') as csvfile:
             writer = csv.DictWriter(csvfile, fieldnames = ["ID", "KEY", "ASSIGNEE","ASSIGNEE-NAME","PRIORITY-NAME","DONE","STATUS-ID","STATUS-NAME","ESTIMATE-STATISTIC","DESCRIPTION"])
             writer.writeheader()
            

             for index in range(issues_l):
                 col_id = (issues[index].get('id', "Not Assigned"))
                 col_key = (issues[index].get('key', "Not Assigned"))
                 col_assignee = (issues[index].get('assignee', "Not Assigned"))
                 col_assigneeName = (issues[index].get('assigneeName', "Not Assigned"))
                 col_priorityName = (issues[index].get('priorityName', "Not Assigned"))
                 col_done = (issues[index].get('done', "Not Assigned"))
                 col_statusId = (issues[index].get('statusId', "Not Assigned"))
                 col_statusName = (issues[index].get('statusName', "Not Assigned"))
                 col_estimateStatistic_value = (issues[index]['estimateStatistic']['statFieldValue'].get('value',"Not Assigned"))
                 col_status_description = (issues[index]['status']['description'])
                 
                 writer.writerow({'ID': col_id, 'KEY': col_key, 'ASSIGNEE': col_assignee ,'ASSIGNEE-NAME': col_assigneeName , 'PRIORITY-NAME': col_priorityName ,'DONE': col_done , 'STATUS-ID': col_statusId ,'STATUS-NAME': col_statusName , 'ESTIMATE-STATISTIC': col_estimateStatistic_value, 'DESCRIPTION': col_status_description})


                 

             
obj=Sprints()
obj.get_current_sprints()
