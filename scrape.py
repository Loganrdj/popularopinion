import os
import tweepy
import config
# import pandas as pd
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
userID = "realDonaldTrump"

# -----------------------------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# -----------------------------------------

tweets = api.user_timeline(screen_name = userID, count = 200, include_rts = False, tweet_mode = "extended")

for info in tweets[:3]:
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id

while True:
    tweets = api.user_timeline(screen_name=userID,
    count=200,
    include_rts=False,
    max_id = oldest_id - 1,
    tweet_mode = "extended")
    if(len(tweets) == 0):
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)

    