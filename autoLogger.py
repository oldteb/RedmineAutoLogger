import io  
import sys
import requests
import json

# <time-entry>
#                 <project-id>30</project-id>
#                 <hours>8</hours>
#                 <activity-id>8</activity-id>
#                 <comments>TEST</comments>
# </time-entry>



def main():
    
    # set the pythons's default encoding to UTF8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    
    payload = {
        'authenticity_token':'u/P+QGJ2UzgLf+cqnBpWiG31Ea25GCtco3b4KO4UVaDjpOaZV47sICPjKwWpFpjwQ186xUfIPFW1Sdjg5s5CSg==',
        'issue_id': 426,
        'time_entry':{
            'comments': 'new featureslala',
            'spent_on': '2017-08-24',
            'hours': '8'
        },
        'commit': 'Create'
    }
    
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection':'keep-alive',
        'content-type': 'application/json',
        'Cookie':'_redmine_session=eWpNY0RBZEVHa0tzZkpwaWZkcmx6cGpNMXZMNFhURjhXSjhtUng1a0FORUg1ckZTOS93TGVocTBlU291RWhmZ3FqU3NUZjZlaUk2L1AyUGg3dEZKN3QzQXc0emY0RW5jMHBvSW9IYno2bHR1MHZXUHQ3dHJBbmFZdThNOXlYUy9YcFh3T3dyWFYyOUs2K2Q3d3lTUnN4RGdHem1vQzhNMW5xT0cwRmd5NkQva3FNSkZtdUJrR1ZpZ3pwRFRpYjBZRENpdDM2S1JJZ1BWSFFpZEM4U25PYmZDSHhSdjZHQThmRUJuTktEc012YVlPR3NHVndVQWVHTUVaVEVraHRYOU5FNnhjUWV5b21JWjAzc1RCRDVPdHFYcUhydnJzTDBqQXdHbXpWYlc5T0pYNHoxb1JSVkFQRnVRWUcvRnVsUWUtLXNiakFWQ3VGZUt6RUkvNWtma3Y5VUE9PQ%3D%3D--a854771231d93b56d32dba842ea9e6deb5f3fcd8'
    }
    
    cookie = {'_redmine_session':'ak9WRXM4TW55T2hGY2hJWFlRZjRqWXkzSVNFVEdOWXFRUmc4WDdoU1dWaWpQMUllWHUzQkhVWW8xSjNVc25vSVlGczU1d0kySlIvRUcwOURWSGxmbFovbitibXlVVTZwMGE0bHdhY1J3NjNDRGhvYVVReXI2NWlFaWZJYncwb05oRXZnMkptMGNzU3dpdVFEVFp4ZGVuYmlOYVc0TkFwZENIeUg5M0R0ekd3eGlHT0dZSURpZERWemtPSkpjSDVMZXpWb0QwZk9PbjZFV1lEU3M0UWEySVp2aUJCVHJZZXo1ZmpGc0JBRXNVV3VIbkZXbm9qYmRuamxJTCs4SFQzQlh4VE56S1R4SXhLcHN4emxrU2VoQUw3eXh1c3dzRG1RcVRrcUpkcmxWQ1FtVysyaU9TeXV4Q0YzQUh2UTVQbnktLTBEbVpqcjVmdTFQQld0VjVvTW9aSFE9PQ%3D%3D--77dd25c4d1f5979cdf1f9f5a55f0dfbb2955751a'}

    
    # r = requests.get("https://10.200.47.218/time_entries", verify=False)
    # print(r.text)
    
    # r = requests.post("https://10.200.47.218/login", data, verify=False)
    
    
    r = requests.post("https://10.200.47.218/time_entries", data=json.dumps(payload), headers=header, verify=False)
    
    
    
    # And done.
    print(r.text) # displays the result body.
    

if __name__ == "__main__":
    main()
