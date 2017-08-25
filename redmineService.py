import requests
import json

def createNewIssue(issue_id, hours, comments):

    header = {
        'X-Redmine-API-Key':'c95029486a22c24bd38972a611e9eb1282a2a023',
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
    

def getIssueName(issue_id):
    header = {'X-Redmine-API-Key':'c95029486a22c24bd38972a611e9eb1282a2a023'}
    r = requests.get('https://10.200.47.218/issues/' + str(issue_id) + '.json', headers=header, verify=False)
    data = r.json()
    return data['issue']['subject']
