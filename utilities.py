import json

        #===============================#
        #      Pokemon Twitter Bot      #
        #===============================#
        
class tokens:
    TOKENS_FILE_PATH = "/Users/brianhockenjos/Desktop/Python_Projects/Global_Variables/Tokens.json"
    API_TOKEN = None
    API_SECRET_TOKEN = None
    BEARER_TOKEN = None
    CLIENT_ID = None
    CLIENT_SECRET_ID = None
    ACCESS_TOKEN = None
    ACCESS_SECRET_TOKEN = None
    BOT_ACCESS_TOKEN = None
    BOT_ACCESS_SECRET_TOKEN = None
    TCG_API_TOKEN = None
    
def setTokens():
    temp_data = readJson(getattr(tokens, 'TOKENS_FILE_PATH'))
    setattr(tokens, "API_TOKEN", temp_data["ADMIN"]["API_TOKEN"])
    setattr(tokens, "API_SECRET_TOKEN", temp_data["ADMIN"]["API_SECRET_TOKEN"])
    setattr(tokens, "BEARER_TOKEN", temp_data["ADMIN"]["BEARER_TOKEN"])
    setattr(tokens, "CLIENT_ID", temp_data["APP1"]["CLIENT_ID"])
    setattr(tokens, "CLIENT_SECRET_ID", temp_data["APP1"]["CLIENT_SECRET_ID"])
    setattr(tokens, "ACCESS_TOKEN", temp_data["APP1"]["ACCESS_TOKEN"])
    setattr(tokens, "ACCESS_SECRET_TOKEN", temp_data["APP1"]["ACCESS_SECRET_TOKEN"])
    setattr(tokens, "BOT_ACCESS_TOKEN", temp_data["APP1"]["BOT_ACCESS_TOKEN"])
    setattr(tokens, "BOT_ACCESS_SECRET_TOKEN", temp_data["APP1"]["BOT_ACCESS_SECRET_TOKEN"])
    setattr(tokens, "TCG_API_TOKEN", temp_data["TCG"]["API_TOKEN"])
    
def readJson(file_path):
    with open (file_path, "r") as file:
        data = json.load(file)  
    return data

def writeJson(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)
    

    
    