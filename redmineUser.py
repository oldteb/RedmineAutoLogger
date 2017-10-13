

class RedmineUser:
    
    def __init__(self, name, userId, APIkey):
        self.name = name
        self.userId = userId
        self.APIkey = APIkey
        
    @classmethod
    def fromConfig(self, config):
        newUser = self.__init__(config["userName"], config["user_id"], config["APIkey"])
        return newUser
        
        
        
