import functions as func
import button as btn
import guesser as guess
import interactive as dm
import tweepy
import random
import pokebase
from gpiozero import Button


"""
    ||===============================||
    ||      Pokemon Twitter Bot      ||
    ||===============================||

    This bot will pull and imagine and data of a pokemon from the Pokemon API,
    It'll then post a tweet containing the picture and the information about the Pokemon.
    - Post a picture of a randomly picked pokemon with some general data about it. --DONE--
    - Interactive dm bot (Play guess that pokemon, or pick a pokemon based on characteristics (maybe))
    - Whose that pokemon random tweet, retweet with answer after certain time elapsed 
    - Whooper Button, a button that when pressed posts a random image of whooper with a random funny quote
    
"""

WHOOPER_BUTTON = Button(18)

def getPokemon():
    temp_data = func.readJson("Pokemon.json")
    #--------------MAJOR ISSUE--------------
    #IF THE POKEMON WAS ALREADY DELETED AND ITS ID IS PICKED AGAIN AN ERROR WILL BE THROWN! MUST FIX
    #MUST FIX func.getRandomMedia() AS WELL! 
    #POSSIBLE FIX WOULD BE ALLOWING POKEMON AND QUOTES TO REPEAT.
    #THIS COULD BE VIABLE FOR POKEMON AS THERE IS 900 OF THEM, 
    #HOWEVER FOR QUOTES THIS MAY NOT BE VIABLE AS THERE WILL BE SO FEW QUOTES.
    poke_dex = random.randint(1, 898) 
    pokemon_name = temp_data[str(poke_dex)]
    #del temp_data[str(poke_dex)]
    #func.writeJson("Pokemon.json", temp_data)
    img = pokebase.SpriteResource('pokemon', poke_dex, other=True, official_artwork=True)
    img_path = img.path
    return poke_dex, pokemon_name, img_path

def getGeneration(id):
    poke_dex = id
    generation = ""
    
    if poke_dex > 0 and poke_dex <= 151:
        generation = "Gen 1"
    elif poke_dex > 151 and poke_dex <= 251:
        generation = "Gen 2"
    elif poke_dex > 251 and poke_dex <= 386:
        generation = "Gen 3"
    elif poke_dex > 386 and poke_dex <= 493:
        generation = "Gen 4"
    elif poke_dex > 493 and poke_dex <= 649:
        generation = "Gen 5"
    elif poke_dex > 649 and poke_dex <= 721:
        generation = "Gen 6"
    elif poke_dex > 721 and poke_dex <= 809:
        generation = "Gen 7"
    elif poke_dex > 809 and poke_dex <= 898:
        generation = "Gen 8"
    else:
        generation = "N/A"
    
    return generation

def formatRandomTweet(id, name):
    NAME = name
    ID = id
    temp_types = []
    pokemon = pokebase.pokemon(ID)
    for types in pokemon.types:
        temp_types.append(types.type.name)
    GENERATION = getGeneration(ID)
    TYPE = ", ".join(temp_types).capitalize()
    formated = \
"Species: {},\n\
Pokedex: {},\n\
Type(s): {},\n\
Generation: {}".format(NAME, ID, TYPE, GENERATION)
    return formated
    
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
    API = api()
    poke_dex, pokemon_name, file_path = getPokemon()
    formated_tweet = formatRandomTweet(poke_dex, pokemon_name)
    tweet(API, formated_tweet, file_path)
    guess.changeIMG(file_path, poke_dex)
    WHOOPER_BUTTON.when_pressed = btn.onButtonPress
