import tweepy

CONSUMER_KEY = "xxx"
CONSUMER_SECRET = "xxx"

oauth1_user_handler = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET,
    callback = "oob"
)

print(oauth1_user_handler.get_authorization_url())

verifier = input("Input PIN: ")
access_token, access_token_secret = oauth1_user_handler.get_access_token(
    verifier
)

print(access_token, access_token_secret)