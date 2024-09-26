import json

def readJS(filePath):
    with open(filePath, 'r') as f:
        return json.load(f)