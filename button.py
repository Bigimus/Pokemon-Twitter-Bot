import functions as func
import main

        #===============================#
        #      Pokemon Twitter Bot      #
        #===============================#

def onButtonPress():
    random_quote = func.getRandomQuote()
    file_path = func.getRandomMedia()
    API = main.api()
    main.tweet(API, random_quote, file_path)
    func.removeFile(file_path)