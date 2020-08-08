import os
import tweepy
import config
import csv
import json
import pandas
from pandas import DataFrame

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
# userID = "realDonaldTrump"
# userID = input("Please input your user ID: ")
queryTerm = input("What would you like to search for? ")

# -----------------------------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# -----------------------------------------

tweets = tweepy.Cursor(api.search, q=queryTerm, lang="en").items(1)
for tweet in tweets:
    print(tweet.text)