import tweepy
import random
import schedule
import time
import sys
import os
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

def create_random_story():
    bodyPart = random.choice(["head", "stomach", "ear", "face", "eye", "nose", "heart", "cheek", "arm", "mouth", "tooth", "leg", "foot", "toe"])
    adj = random.choice(["blackens and curls", "crumbles", "grows huge", "crawls", "is eaten", "melts", "falls off", "turns into nothing", "shines in the dark", "disappears", "turns black"])
    person = random.choice(["father", "mother", "sister", "brother", "teacher", "co-worker", "manager", "son", "daughter"])
    action = random.choice(["die", "fly away", "leave", "smile", "frown", "laugh", "melt", "disappear", "chuckle"])
    place = random.choice(["with a rose", "with a sunflower", "with an old friend", "with an old enemy", "with your journal", "with your diary", "with oil paints", "with a mango", "with yourself", "with another", "in the searing desert", "in your home", "in the mall", "in the park", "outside", "inside", "in your parent's bedroom", "in the southeast corner of your old school"])
    des = random.choice(["favorite", "neglected", "beloved", "huge", "small"])
    final = random.choice(["forever", "without a word", "silently", "quickly", "spontaneously", "over and over again", "badly"])

    intro1 = "Your " + bodyPart + " " + adj + ", as you watch your " + person + " " + action + " " + final + "."
    intro2 = "Alone " + place + ", your " + des + " " + bodyPart + " " + adj + "."
    intro3 = "You didn't expect your " + person + " to point out your " + des + " " + bodyPart + "."

    intros = [intro1, intro2, intro3]
    story = random.choice(intros)
    print(story)
    return story


def job():
    api.update_status(create_random_story())




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

schedule.every().minute.do(job)

# $ run the schedule
while 1:
    schedule.run_pending()
    time.sleep(15)
