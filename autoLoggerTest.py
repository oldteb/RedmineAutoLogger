import io  
import sys
import requests
import json
import getpass
import datetime
import time
import holidays

from redmineService import RedmineService
from redmineAPI import RedmineAPI
from redmineUser import RedmineUser
from timeEntry import TimeEntry
import autoLogger


def testGetTimeEntriesInRange():
    timeEntriesObj = api.getTimeEntriesInRange(userYT, '2017-09-01', '2017-09-20')
    print(timeEntriesObj)
    

def testLogTime():
    newTimeEntry = TimeEntry(30,426,'2017-10-13',8,'testCreateNewIssue2')
    api.logTime(userYT, newTimeEntry)
    
    
def testFillMissingLogs():
    timeEntry = TimeEntry(30,426,'2017-10-13',8,'testCreateNewIssue2')
    service.fillMissingLogs(userYT, timeEntry, '2017-09-01', '2017-09-30')


def testIsDateToLog():
    rst = service.isDateToLog('2017-10-06')
    # print(rst)

def testUpdateRedmine():
    config = {
    	"APIkey":"c95029486a22c24bd38972a611e9eb1282a2a023",
    	"userName": "YTang",
    	"project_id": 30,
    	"issue_id": 426,
    	"user_id": 23,
    	"hours": 8,
    	"comments": "Working on QMS; add purchase order."
    }
    autoLogger.updateRedmine(config, service)
    
    

def main():
    global userYT
    global api
    global service
    print('test start!')
    userYT = RedmineUser('YTang',23,'c95029486a22c24bd38972a611e9eb1282a2a023')
    api = RedmineAPI()
    service = RedmineService()
    # testGetTimeEntriesInRange()
    # testLogTime()
    # testFillMissingLogs()
    # testIsDateToLog()
    testUpdateRedmine()
    
    print('test complete!')

if __name__ == "__main__":
    main()
