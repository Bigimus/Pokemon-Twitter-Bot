import functions as func
"""
    ||===============================||
    ||      Pokemon Twitter Bot      ||
    ||===============================||

    This bot will pull and imagine and data of a pokemon from the Pokemon API,
    It'll then post a tweet containing the picture and the information about the Pokemon.
    consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
"""

if __name__ == "__main__":
    func.setTokens()