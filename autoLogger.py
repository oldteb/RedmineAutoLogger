import io  
import sys
import requests
import json
import getpass
from datetime import datetime, date, timedelta
import time

from redmineService import RedmineService
from redmineUser import RedmineUser
from timeEntry import TimeEntry



def loadFromConfig():
    file = open("config.json", "r") 
    jsonStr = file.read()
    return json.loads(jsonStr)


def logAction(msg):
    file = open("log.txt", "a") 
    file.write(msg + "\n")


def updateRedmine(config, service):
    user = RedmineUser.fromConfig(config)
    timeEntry = TimeEntry.fromConfig(config)
    
    startDate = (datetime.today() - timedelta(days=15)).date()
    endDate = datetime.today().date()
    
    # print(startDate)
    # print(endDate)
    service.fillMissingLogs(user, timeEntry, str(startDate), str(endDate))
    
    
# take a x mins break
def takeBreak():
    time.sleep(1*60)


    
def main():
    print('Redmine Auto Logger starts')
    # # set the pythons's default encoding to UTF8
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

    isWorking = False
    logged = False
    
    while(True):
        takeBreak()
        service = RedmineService()
        config = loadFromConfig()
        now = datetime.now()
        
        if now.hour == 0:
            isWorking = False
            logged = False
        
        # skip weekend & holidays
        if service.isDateToLog(str(now.date())) == False:
            continue
        
        # skip if not in working hours
        if now.hour < 9 or now.hour > 18:
            continue
        
        # skip if user is not log in
        if getpass.getuser() == userName:
            isWorking = True
            
        # log time at 4:00PM
        if now.hour == 16 and isWorking == True and logged == False:
            updateRedmine(config, service)
            logged = True
            
    print('Redmine Auto Logger exits')


if __name__ == "__main__":
    main()
