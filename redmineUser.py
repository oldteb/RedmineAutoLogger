

class RedmineUser:
    
    def __init__(self, name, userId, APIkey):
        self.name = name
        self.userId = userId
        self.APIkey = APIkey
        
    @classmethod
    def fromConfig(cls, config):        
        return cls(config["userName"], config["user_id"], config["APIkey"])
        
        
        
