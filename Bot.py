import tweepy
import time
from answer import read_last_seen, interact

consumer_key = 'your key'
consumer_secret = 'your secret key'
access_token = 'your token'
access_token_secret = 'your secret token'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
while True:
    FILE_NAME = 'last_seen.txt'
    api = tweepy.API(auth)
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    interact(tweets, api, FILE_NAME)
    time.sleep(120)