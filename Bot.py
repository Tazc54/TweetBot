import tweepy
from answer import retweetHashtag, read_last_seen, store_last_seen

consumer_key = 'Your Key'
consumer_secret = 'your secret'
access_token = 'your token'
access_token_secret = 'your token secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweets = api.mentions_timeline()

#retweetHashtag(tweets, api)

