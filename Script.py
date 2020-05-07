import tweepy
import random
import time
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']


def follow_back():
    followers = tweepy.Cursor(api.followers).items()
    following = tweepy.Cursor(api.friends).items()
    for follower in followers:
        if follower in following:
            print('did nothing for one person')
        else:
            follower.follow()
            print('followed : ' + follower.screen_name)


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

    noun = random.choice(["He", "She", "It"])

    descriptionFinal = random.choice(["lovingly", "menacingly", "carefully", "quietly"])

    verb = random.choice(["thinks", "decides", "watches", "stares", "gazes", "smiles", "frowns", "laughs"])

    actionPlural = random.choice(["strokes", "grabs", "crushes", "holds", "caresses"])

    verb2 = random.choice(["thinks", "decides", "watches", "stares", "gazes", "smiles", "frowns", "laughs"])

    pensive = random.choice(["wondering why", "questioning why", "pondering why"])

    sudden = random.choice(["suddenly", "quietly", "amazingly", "quickly"])

    explodes = random.choice(["exploded into", "unfurled into", "became", "changed into"])

    number = random.choice(["two", "seventeen", "sixty-four", "two million", "seventy-five billion"])

    things = random.choice(["butterflies", "colors", "intricate hand carved wooden horses", "carrots", "diamonds"])

    nounKnown = random.choice(
        ["The old man", "The old woman", "The demon", "The angel", "The magician", "The ghostly figure"])

    nounKnown2 = random.choice(
        ["the old man's", "the old woman's", "the demon's", "the angel's", "the magician's", "the ghostly figure's"])

    intro1 = "Your " + bodyPart + " " + adj + ", as you watch your " + person + " " + action + " " + final + "."
    intro2 = "Alone " + context + ", your " + des + " " + bodyPart + " " + adj + "."
    intro3 = "You didn't expect your " + person + " to point out your " + des + " " + bodyPart + "."
    intro4 = noun + " " + verb + ", as " + noun.lower() + " " + actionPlural + " your " + bodyPart + " " + descriptionFinal + "."
    intro5 = nounKnown + " " + verb + " and " + verb2 + ", " + pensive + " " + nounKnown2 + " " + bodyPart + " " + sudden + " " + explodes + " " + number + " " + things + "."

    intros = [intro1, intro2, intro3, intro4, intro5]
    story1 = random.choice(intros)
    print(story1)
    return story1


# Authenticate to Twitter
# telling Tweepy to use the credentials that created
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creates an API object that you can use to invoke Twitter API methods. Setting wait_on_rate_limit and wait_on_
# rate_limit_notify to True makes the API object print a message and wait if the rate limit is exceeded
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

interval = 60 * 60 * 4
# $ run the schedule
while True:
    print("Making story...")
    story = create_random_story()
    api.update_status(story)
    follow_back()
    time.sleep(interval)
