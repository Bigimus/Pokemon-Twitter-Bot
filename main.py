import functions as func
import tweepy
from requests_oauthlib import OAuth1
"""
    ||===============================||
    ||      Pokemon Twitter Bot      ||
    ||===============================||

    This bot will pull and imagine and data of a pokemon from the Pokemon API,
    It'll then post a tweet containing the picture and the information about the Pokemon.
"""

def api():
    temp_API_TOKEN = func.getAPI()
    temp_API_SECRET_TOKEN = func.getAPISecret()
    temp_BOT_ACCESS_TOKEN = func.getBotAccess()
    temp_BOT_ACCESS_SECRET_TOKEN = func.getBotAccessSecret()
    auth = tweepy.OAuthHandler(temp_API_TOKEN, temp_API_SECRET_TOKEN)
    auth.set_access_token(temp_BOT_ACCESS_TOKEN, temp_BOT_ACCESS_SECRET_TOKEN)
    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path = None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)
        
    print("Sent a Tweet successfully")
    
if __name__ == "__main__":
    func.setTokens()
    api = api()
    tweet(api, "TEST TWEET")