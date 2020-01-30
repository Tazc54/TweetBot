import tweepy

consumer_key = 'Your Key'
consumer_secret = 'your secret'
access_token = 'your token'
access_token_secret = 'your token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_status('bot second tweet with python and tweepy.')
