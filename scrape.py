import os
import tweepy
import config
import csv
import json
import pandas
import unicodedata
from pandas import DataFrame
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Popinion
# Vader Sentiment analysis

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret
# userID = "realDonaldTrump"
# userID = input("Please input your user ID: ")
queryTerm = raw_input("What would you like to search for? ")
queryTerm += "-filter:retweets"
# -----------------------------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# -----------------------------------------

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    # print("{:-<40} {}".format(sentence, str(score)))
    return score

tweets = tweepy.Cursor(api.search, q=queryTerm, lang="en").items(500)
totalCount = 0
totalNeg = 0
totalPos = 0
totalNeutral = 0
totalMixture = 0
totalUnknown = 0

print("Please wait a moment!")
print("")
print("Loading...")

for tweet in tweets:
    # print(tweet.text)
    totalCount += 1.0
    newTweet = tweet.text.encode('ascii', 'ignore')
    # print(sentiment_analyzer_scores(newTweet))
    score = sentiment_analyzer_scores(newTweet)
    if(score['neg'] > score['pos']):
        totalNeg = totalNeg + 1.0
    elif(score['pos'] > score['neg']):
        totalPos = totalPos + 1.0
    else:
        totalUnknown += 1.0

# print(totalCount)
# print(totalNeg)
# print(totalPos)
# print(totalUnknown)
resultPos = totalPos/totalCount * 100.0
resultNeg = totalNeg/totalCount * 100.0
resultUnknown = totalUnknown/totalCount * 100.0

print("Out of {} tweets,").format(totalCount)
print("Negative Opinions: {}%").format(resultNeg)
print("Positive Opinions: {}%").format(resultPos)
print("Neutral/Unknown Opinions: {}%").format(resultUnknown)
