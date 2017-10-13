
class TimeEntry:
    
    def __init__(self,issueId, date, hours, comments,id=-1):
        self.id = id
        self.issueId = issueId
        self.date = date
        self.hours = hours
        self.comments = comments
        
