import io  
import sys
import requests
import json

from timeEntry import TimeEntry


class RedmineAPI:


    def __init__(self):
        pass

    # This method return all the time entries that within the given time range(inclusive).
    # The startTime and endTime string must be in format of 'yyyy-MM-dd'
    def getTimeEntriesInRange(self, user, startTime, endTime):
        header = {
            'X-Redmine-API-Key': user.APIkey,
            'Content-Type': 'application/xml'
        }
        queryStr = ('time_entries.json?user_id=' + str(user.userId) +  '&spent_on=><' +
            startTime + '|' + endTime 
        )
        r = requests.get("https://10.200.47.218/" + queryStr, headers=header, verify=False)
        timeEntriesObj = json.loads(r.content.decode("utf-8"))
        # print(timeEntriesObj["total_count"])
        return timeEntriesObj
    
    
    
    # This method logs a new time entry.
    def logTime(self, user, timeEntry):
        header = {
            'X-Redmine-API-Key': user.APIkey,
            'Content-Type': 'application/json'
        }
        newTimeEntry = {}
        newTimeEntry["project_id"] = timeEntry.projectId
        newTimeEntry["issue_id"] = timeEntry.issueId
        newTimeEntry["hours"] = timeEntry.hours
        newTimeEntry["comments"] = timeEntry.comments
        newTimeEntry["spent_on"] = timeEntry.date
        payload = {}
        payload["time_entry"] = newTimeEntry
        payloadStr = json.dumps(payload)
        # print(payloadStr)
        r = requests.post("https://10.200.47.218/time_entries.json", data=payloadStr, headers=header, verify=False)
        responseObj = json.loads(r.content.decode("utf-8"))
        print('Successfully create new time entry: ' + str(responseObj["time_entry"]["id"]))
        # print(r.content)
        return
    
    
    
    # This method is abandont because it use xml format.
    # New method is logTime(), which is implement using json.
    # This method logs a new time entry.
    def createNewIssue(self, user, timeEntry):
        header = {
            'X-Redmine-API-Key': user.APIkey,
            'Content-Type': 'application/xml'
        }
        payload = ("<time-entry><issue_id>" + str(timeEntry.issueId) + 
            "</issue_id><hours>" + str(timeEntry.hours) + "</hours><comments>" + 
            timeEntry.comments + "</comments></time-entry>"
        )
        r = requests.post("https://10.200.47.218/time_entries.xml", data=payload, headers=header, verify=False)
        # print('Successfully create new issue: ' + str())
        print(r.content)
        
        return
        
        
        
    # Not used for now
    def createNewIssueHard(self, issue_id, hours, comments):
        payload = {
            'authenticity_token':'u/P+QGJ2UzgLf+cqnBpWiG31Ea25GCtco3b4KO4UVaDjpOaZV47sICPjKwWpFpjwQ186xUfIPFW1Sdjg5s5CSg==',
            'issue_id': issue_id,
            'time_entry':{
                'comments': comments,
                'hours': hours
            },
            'commit': 'Create'
        }
        header = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection':'keep-alive',
            'content-type': 'application/json',
            'Cookie':'_redmine_session=eWpNY0RBZEVHa0tzZkpwaWZkcmx6cGpNMXZMNFhURjhXSjhtUng1a0FORUg1ckZTOS93TGVocTBlU291RWhmZ3FqU3NUZjZlaUk2L1AyUGg3dEZKN3QzQXc0emY0RW5jMHBvSW9IYno2bHR1MHZXUHQ3dHJBbmFZdThNOXlYUy9YcFh3T3dyWFYyOUs2K2Q3d3lTUnN4RGdHem1vQzhNMW5xT0cwRmd5NkQva3FNSkZtdUJrR1ZpZ3pwRFRpYjBZRENpdDM2S1JJZ1BWSFFpZEM4U25PYmZDSHhSdjZHQThmRUJuTktEc012YVlPR3NHVndVQWVHTUVaVEVraHRYOU5FNnhjUWV5b21JWjAzc1RCRDVPdHFYcUhydnJzTDBqQXdHbXpWYlc5T0pYNHoxb1JSVkFQRnVRWUcvRnVsUWUtLXNiakFWQ3VGZUt6RUkvNWtma3Y5VUE9PQ%3D%3D--a854771231d93b56d32dba842ea9e6deb5f3fcd8'
        }
        r = requests.post("https://10.200.47.218/time_entries", data=json.dumps(payload), headers=header, verify=False)
        
        

    def getIssueName(self, issue_id, APIkey):
        header = {'X-Redmine-API-Key': APIkey}
        r = requests.get('https://10.200.47.218/issues/' + str(issue_id) + '.json', headers=header, verify=False)
        data = r.json()
        return data['issue']['subject']
