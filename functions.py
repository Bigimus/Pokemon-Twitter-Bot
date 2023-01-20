import json

FILE_PATH = "/Users/brianhockenjos/Desktop/Python_Projects/Global_Variables/Tokens.json"
API_TOKEN = ""
API_SECRET_TOKEN = ""
BEARER_TOKEN = ""
CLIENT_ID = ""
CLIENT_SECRET_ID = ""
ACCESS_TOKEN = ""
ACCESS_SECRET_TOKEN = ""
BOT_ACCESS_TOKEN = ""
BOT_ACCESS_SECRET_TOKEN = ""

def getData():
    with open (FILE_PATH, "r") as file:
        temp_data = json.load(file)  
    return temp_data

def setAPI(token):
    global API_TOKEN
    API_TOKEN = token
    return API_TOKEN

def setAPISecret(token):
    global API_SECRET_TOKEN
    API_SECRET_TOKEN = token
    return API_SECRET_TOKEN

def setBearer(token):
    global BEARER_TOKEN
    BEARER_TOKEN = token
    return BEARER_TOKEN

def setClient(ID):
    global CLIENT_ID
    CLIENT_ID = ID
    return CLIENT_ID

def setClientSecret(ID):
    global CLIENT_SECRET_ID
    CLIENT_SECRET_ID = ID
    return CLIENT_SECRET_ID

def setAccess(token):
    global ACCESS_TOKEN
    ACCESS_TOKEN = token
    return ACCESS_TOKEN

def setAccessSecret(token):
    global ACCESS_SECRET_TOKEN
    ACCESS_SECRET_TOKEN = token
    return ACCESS_SECRET_TOKEN

def setBotAccess(token):
    global BOT_ACCESS_TOKEN
    BOT_ACCESS_TOKEN = token
    return BOT_ACCESS_TOKEN

def setBotAccessSecret(token):
    global BOT_ACCESS_SECRET_TOKEN
    BOT_ACCESS_SECRET_TOKEN = token
    return BOT_ACCESS_SECRET_TOKEN

def setTokens():
    temp_data = getData()
    setAPI(temp_data["ADMIN"]["API_TOKEN"])
    setAPISecret(temp_data["ADMIN"]["API_SECRET_TOKEN"])
    setBearer(temp_data["ADMIN"]["BEARER_TOKEN"])
    setClient(temp_data["APP1"]["CLIENT_ID"])
    setClientSecret(temp_data["APP1"]["CLIENT_SECRET_ID"])
    setAccess(temp_data["APP1"]["ACCESS_TOKEN"])
    setAccessSecret(temp_data["APP1"]["ACCESS_SECRET_TOKEN"])
    setBotAccess(temp_data["APP1"]["BOT_ACCESS_TOKEN"])
    setBotAccessSecret(temp_data["APP1"]["BOT_ACCESS_SECRET_TOKEN"])
    
def getAPI():
    global API_TOKEN
    return API_TOKEN
    
def getAPISecret():
    global API_SECRET_TOKEN
    return API_SECRET_TOKEN

def getBEARER():
    global BEARER_TOKEN
    return BEARER_TOKEN

def getClient():
    global CLIENT_ID
    return CLIENT_ID

def getClientSecret():
    global CLIENT_SECRET_ID
    return CLIENT_SECRET_ID

def getAccess():
    global ACCESS_TOKEN
    return ACCESS_TOKEN

def getAccessSecret():
    global ACCESS_SECRET_TOKEN
    return ACCESS_SECRET_TOKEN

def getBotAccess():
    global BOT_ACCESS_TOKEN
    return BOT_ACCESS_TOKEN

def getBotAccessSecret():
    global BOT_ACCESS_SECRET_TOKEN
    return BOT_ACCESS_SECRET_TOKEN