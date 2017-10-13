import io  
import sys
import json
from datetime import datetime
from datetime import date, timedelta
import time
import holidays

from redmineAPI import RedmineAPI
from redmineUser import RedmineUser
from timeEntry import TimeEntry



class RedmineService:

    def __init__(self):
        self.api = RedmineAPI()
        self.us_holidays = holidays.UnitedStates()
    
    
    # find and log time for all dates that log is missing.
    # only dates in range [startTime, endTime] is checked.
    def fillMissingLogs(self, user, timeEntry, startTime, endTime):
        timeLogsObj = self.api.getTimeEntriesInRange(user, startTime, endTime)
        logDates = self.__getLoggedDates(timeLogsObj)
        datesBetween = self.__getDatesBetween(startTime, endTime)
        unlogDates = []             # find all dates that log is missing
        for date in datesBetween:
            if date not in logDates:
                unlogDates.append(date)
        
        for date in unlogDates:
            if self.isDateToLog(date):
                timeEntry.date = date
                self.api.logTime(user, timeEntry)
        return
    
    
    # find if time should be logged or not on a specific day.
    # for example, weekend and holiday should be skipped.
    def isDateToLog(self, dateStr):
        pattern = '%Y-%m-%d'
        date = datetime.strptime(dateStr, pattern).date()
        # skip weekend
        if date.weekday() > 4:   # 4 is Friday
            return False
        # skip national holildays
        if date in self.us_holidays:
            return False
        return True
    
    
    # private method
    def __getLoggedDates(self, timeLogsObj):
        logs = timeLogsObj["time_entries"]
        logDates = {}
        for log in logs:
            date = log["spent_on"]
            logDates[date] = 1
        return logDates
        

    def __getDatesBetween(self, startTime, endTime):
        pattern = '%Y-%m-%d'
        d1 = datetime.strptime(startTime, pattern).date()
        d2 = datetime.strptime(endTime, pattern).date()
        delta = d2 - d1         # timedelta
        datesBetween = []
        for i in range(delta.days + 1):
            date = d1 + timedelta(days=i)
            datesBetween.append(str(date))
        return datesBetween
    
    
