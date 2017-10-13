
class TimeEntry:
    
    def __init__(self, projectId, issueId, date, hours, comments,id=-1):
        self.id = id
        self.projectId = projectId
        self.issueId = issueId
        self.date = date
        self.hours = hours
        self.comments = comments
        
        
    @classmethod
    def fromConifg(self, config):
        timeEntry = self.__init__(
            config["project_id"], 
            config["issue_id"],
            "1970-01-01",
            config["hours"],
            config["comments"]
            )
            
        return timeEntry
        
        
