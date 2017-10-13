import io  
import sys
import requests
import json
import getpass
import datetime
import time
import holidays

from redmineAPI import RedmineAPI
from redmineUser import RedmineUser
from timeEntry import TimeEntry


def testGetTimeEntriesInRange():
    timeEntriesObj = api.getTimeEntriesInRange(userYT, '2017-09-01', '2017-09-20')
    # print(timeEntries)
    


def testLogTime():
    newTimeEntry = TimeEntry(30,426,'2017-10-13',8,'testCreateNewIssue2')
    api.logTime(userYT, newTimeEntry)
    


def main():
    global userYT
    global api
    userYT = RedmineUser('YTang',23,'c95029486a22c24bd38972a611e9eb1282a2a023')
    api = RedmineAPI()
    # testGetTimeEntriesInRange()
    testLogTime()


if __name__ == "__main__":
    main()
