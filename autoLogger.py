import requests
    
def main():
    
    data = {
        'authenticity_token':'HgsZHJNETAL2K/MpD7TVcW3x7WylxgdSSJoYhyt0Fa7GtUCgh2cnbHIDSVST0OwqcJrvUb/wKT73oOEgXckaqw==',
        'issue_id': 426,
        'time_entry':{
            'comments': 'new features1',
            'spent_on': '2017-08-22',
            'hours': '8'
        },
        'commit': 'Create'
    }
    
    r = requests.post("https://10.200.47.218/time_entries", data)
    
    # And done.
    print(r.text) # displays the result body.
    

if __name__ == "__main__":
    main()
