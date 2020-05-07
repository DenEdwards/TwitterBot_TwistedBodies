import tweepy
import random
import time
from credentials import consumer_key, consumer_secret, access_token_secret, access_token


def create_random_story():
    bodyPart = random.choice(
        ["head", "stomach", "ear", "face", "eye", "nose", "heart", "cheek", "arm", "mouth", "tooth", "leg", "foot",
         "toe"])

    adj = random.choice(["blackens and curls", "crumbles", "grows huge", "crawls", "is eaten", "melts", "falls off",
                         "turns into nothing", "shines in the dark", "disappears", "turns black"])

    person = random.choice(
        ["father", "mother", "sister", "brother", "teacher", "co-worker", "manager", "son", "daughter"])

    action = random.choice(["die", "fly away", "leave", "smile", "frown", "laugh", "melt", "disappear", "chuckle"])

    context = random.choice(
        ["with a rose", "with a sunflower", "with an old friend", "with an old enemy", "with your journal",
         "with your diary", "with oil paints", "with a mango", "with yourself", "with another", "in the searing desert",
         "in your home", "in the mall", "in the park", "outside", "inside", "in your parent's bedroom",
         "in the southeast corner of your old school"])

    des = random.choice(["favorite", "neglected", "beloved", "huge", "small"])

    final = random.choice(
        ["forever", "without a word", "silently", "quickly", "spontaneously", "over and over again", "badly"])

    noun = random.choice(["He", "She", "It"])#

    descriptionFinal = random.choice(["lovingly", "menacingly", "carefully", "quietly"])#

    verb = random.choice(["thinks", "decides", "watches", "stares", "gazes", "smiles", "frowns", "laughs"])


    actionPlural = random.choice(["strokes", "grabs", "crushes", "holds", "caresses"])#

    #############################################################################################################################
    verb2 = random.choice(["thinks", "decides", "watches", "stares", "gazes", "smiles", "frowns", "laughs"])

    pensive = random.choice(["wondering why", "questioning why", "pondering why"])

    sudden = random.choice(["suddenly", "quietly", "amazingly", "quickly"])

    explodes = random.choice(["exploded into", "unfurled into", "became", "changed into"])

    number = random.choice(["two", "seventeen", "sixty-four", "two million", "seventy-five billion"])

    things = random.choice(["butterflies", "colors", "intricate hand carved wooden horses", "carrots", "diamonds"])

    nounKnown = random.choice(["The old man", "The old woman", "The demon", "The angel", "The magician", "The ghostly figure"])#
    nounKnown2 = random.choice(["the old man's", "the old woman's", "the demon's", "the angel's", "the magician's", "the ghostly figure's"])#

################################################################################################################################
    intro5 = nounKnown + " " + verb + " and " + verb2 + ", " + pensive + " " + nounKnown2 + " " + bodyPart + " " + sudden + " " + explodes + " " + number + " " + things + "."#

    print(intro5)


create_random_story()
