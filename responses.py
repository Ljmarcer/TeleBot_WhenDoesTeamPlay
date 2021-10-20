import re
import looker
from telegram.ext import *


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]

## Aqui van todos los equipos 
def madrid():
    return looker.getvalues('https://fbref.com/en/squads/53a2f082/2021-2022/matchlogs/all_comps/schedule/Real-Madrid-Scores-and-Fixtures-All-Competitions','Real Madrid')
   
def atmadrid():
    return looker.getvalues('https://fbref.com/en/squads/db3b9613/2021-2022/matchlogs/all_comps/schedule/Atletico-Madrid-Scores-and-Fixtures-All-Competitions', 'At Madrid')

def barca():
    return looker.getvalues('https://fbref.com/en/squads/206d90db/2021-2022/matchlogs/all_comps/schedule/Barcelona-Scores-and-Fixtures-All-Competitions', 'Barça')

def valencia():
    return looker.getvalues('https://fbref.com/en/squads/dcc91a7b/2021-2022/matchlogs/all_comps/schedule/Valencia-Scores-and-Fixtures-All-Competitions',' Valencia')

def mancity():
    return looker.getvalues('https://fbref.com/en/squads/b8fd03ef/2021-2022/matchlogs/all_comps/schedule/Manchester-City-Scores-and-Fixtures-All-Competitions', 'Man City')

def manun():
    return looker.getvalues('https://fbref.com/en/squads/19538871/2021-2022/matchlogs/all_comps/schedule/Manchester-United-Scores-and-Fixtures-All-Competitions','Man United')

def sevilla():
    return looker.getvalues('https://fbref.com/en/squads/ad2be733/2021-2022/matchlogs/all_comps/schedule/Sevilla-Scores-and-Fixtures-All-Competitions','Sevilla FC')

def villa():
    return looker.getvalues('https://fbref.com/en/squads/2a8183b3/2021-2022/matchlogs/all_comps/schedule/Villareal-Scores-and-Fixtures-All-Competitions','Villareal')

def psg():
    return looker.getvalues('https://fbref.com/en/squads/e2d8892c/2021-2022/matchlogs/all_comps/schedule/Paris-Saint-Germain-Scores-and-Fixtures-All-Competitions','Psg')

def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there!'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        process_message(message, ['your', 'name'], 'My name is Mario, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you!'),
        process_message(message, ['when', 'does','real','madrid','play'],madrid()),
        process_message(message, ['when', 'does','Barcelona','barça','barsa','play'],barca()),
        process_message(message, ['when', 'does','valencia','play'],valencia()),
        process_message(message, ['when', 'does','city','manchester','man','play'],mancity()),
        process_message(message, ['when', 'does','united','manchester','man','play'],manun()),
        process_message(message, ['when', 'does','atletico','madrid','play'],atmadrid()),
        process_message(message, ['when', 'does','sevilla','play'],sevilla()),
        process_message(message, ['when', 'does','villareal','play'],villa()),
        process_message(message, ['when', 'does','psg','paris','play'],psg()),


        # Add more responses here
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')