

def loadFromConfig():
    file = open('config.json', 'r') 
    jsonStr = file.read()
    return json.loads(jsonStr)
