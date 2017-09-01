import io  
import sys
import requests
import json
import getpass
import datetime
import time

import redmineService

def loadFromConfig():
    file = open("config.json", "r") 
    jsonStr = file.read()
    return json.loads(jsonStr)


def logAction(msg):
    file = open("log.txt", "a") 
    file.write(msg + "\n")


def createNewIssue(issue_id, hours, comments, APIkey):
    header = {
        'X-Redmine-API-Key': APIkey,
        'Content-Type': 'application/xml'
    }
    payload = "<time-entry><issue_id>" + str(issue_id) + "</issue_id><hours>" + str(hours) + "</hours><comments>" + comments + "</comments></time-entry>"
    r = requests.post("https://10.200.47.218/time_entries.xml", data=payload, headers=header, verify=False)
    return r
    
    
def createNewIssueHard(issue_id, hours, comments):
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
    

def getIssueName(issue_id, APIkey):
    header = {'X-Redmine-API-Key': APIkey}
    r = requests.get('https://10.200.47.218/issues/' + str(issue_id) + '.json', headers=header, verify=False)
    data = r.json()
    return data['issue']['subject']
    
    
def main():
    print('Redmine Auto Logger starts')
    # # set the pythons's default encoding to UTF8
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    isWorking = False
    logged = False
    while(True):
        config = loadFromConfig()
        userName = config["userName"]
        issue_id = config["issue_id"]
        hours = config["hours"]
        comments = config["comments"]
        APIkey = config["APIkey"]
                
        now = datetime.datetime.now()
        today = datetime.datetime.today()
        
        if now.hour == 0:
            isWorking = False
            logged = False
        # skip weekend
        if today.weekday() > 4:   # 4 is Friday
            time.sleep(1*60)
            continue
        # skip if not in working hours
        if now.hour < 9 or now.hour > 18:
            time.sleep(1*60)
            continue

        if getpass.getuser() == userName:
            isWorking = True
            
        # log time at 4:00PM
        if now.hour == 16 and isWorking == True and logged == False:
            logAction("[" + time.strftime("%m-%d-%y %H:%M %a") + "] issue id:" + str(issue_id) + ", hours:" + str(hours) + ", comments:" + comments)
            redmineService.createNewIssue(issue_id, hours, comments)
            logged = True
        
        # take a x mins break
        time.sleep(1*60) 
    
    print('Redmine Auto Logger exits')

if __name__ == "__main__":
    main()
