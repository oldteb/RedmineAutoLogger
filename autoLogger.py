import io  
import sys
import requests
import json
import getpass
import datetime
import time
import holidays

from redmineAPI import RedmineAPI



def loadFromConfig():
    file = open("config.json", "r") 
    jsonStr = file.read()
    return json.loads(jsonStr)


def logAction(msg):
    file = open("log.txt", "a") 
    file.write(msg + "\n")
    
    
def main():
    print('Redmine Auto Logger starts')
    # # set the pythons's default encoding to UTF8
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    
    api = RedmineAPI()
    
    isWorking = False
    logged = False
    while(True):
        us_holidays = holidays.UnitedStates()
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
        
        # skip national holildays
        if today in us_holidays:
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
            api.createNewIssue(issue_id, hours, comments)
            logged = True
        
        # take a x mins break
        time.sleep(1*60) 
    
    print('Redmine Auto Logger exits')


if __name__ == "__main__":
    main()
