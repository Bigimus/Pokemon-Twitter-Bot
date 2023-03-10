import json
import os
import random
import BrainlyQuote as BQ

        #===============================#
        #      Pokemon Twitter Bot      #
        #===============================#

TOKENS_FILE_PATH = "/Users/brianhockenjos/Desktop/Python_Projects/Global_Variables/Tokens.json"
WHOOPER_FILE_PATH = "Whooper_Images/"
API_TOKEN = ""
API_SECRET_TOKEN = ""
BEARER_TOKEN = ""
CLIENT_ID = ""
CLIENT_SECRET_ID = ""
ACCESS_TOKEN = ""
ACCESS_SECRET_TOKEN = ""
BOT_ACCESS_TOKEN = ""
BOT_ACCESS_SECRET_TOKEN = ""
TCG_API_TOKEN = ""

def readJson(file_path):
    with open (file_path, "r") as file:
        data = json.load(file)  
    return data

def writeJson(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)
        
def removeFile(file_path):
    os.remove(file_path)
    
def setTokens():
    temp_data = readJson(TOKENS_FILE_PATH)
    setAPI(temp_data["ADMIN"]["API_TOKEN"])
    setAPISecret(temp_data["ADMIN"]["API_SECRET_TOKEN"])
    setBearer(temp_data["ADMIN"]["BEARER_TOKEN"])
    setClient(temp_data["APP1"]["CLIENT_ID"])
    setClientSecret(temp_data["APP1"]["CLIENT_SECRET_ID"])
    setAccess(temp_data["APP1"]["ACCESS_TOKEN"])
    setAccessSecret(temp_data["APP1"]["ACCESS_SECRET_TOKEN"])
    setBotAccess(temp_data["APP1"]["BOT_ACCESS_TOKEN"])
    setBotAccessSecret(temp_data["APP1"]["BOT_ACCESS_SECRET_TOKEN"])
    setTCGAPI(temp_data["TCG"]["API_TOKEN"])
    
def setAPI(token):
    global API_TOKEN
    API_TOKEN = token

def setAPISecret(token):
    global API_SECRET_TOKEN
    API_SECRET_TOKEN = token

def setBearer(token):
    global BEARER_TOKEN
    BEARER_TOKEN = token

def setClient(ID):
    global CLIENT_ID
    CLIENT_ID = ID

def setClientSecret(ID):
    global CLIENT_SECRET_ID
    CLIENT_SECRET_ID = ID

def setAccess(token):
    global ACCESS_TOKEN
    ACCESS_TOKEN = token

def setAccessSecret(token):
    global ACCESS_SECRET_TOKEN
    ACCESS_SECRET_TOKEN = token

def setBotAccess(token):
    global BOT_ACCESS_TOKEN
    BOT_ACCESS_TOKEN = token

def setBotAccessSecret(token):
    global BOT_ACCESS_SECRET_TOKEN
    BOT_ACCESS_SECRET_TOKEN = token

def setTCGAPI(token):
    global TCG_API_TOKEN
    TCG_API_TOKEN = token
    
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

def getTCGAPI():
    global TCG_API_TOKEN
    return TCG_API_TOKEN

def getRandomMedia():
    random_image = random.choice(os.listdir("Whooper_Images"))
    file_path = f"Whooper_Images/{random_image}"
    return file_path
    
def getRandomQuote():
    temp_data = readJson("Categories.json")
    idx = random.randint(0, 124)
    random_category = temp_data[str(idx-1)]
    quotes_list = BQ.quotes(random_category, 125)
    
    if len(quotes_list) > idx:
        idx = random.randint(0,len(quotes_list))
        
    random_quote = quotes_list[idx]
    return random_quote


