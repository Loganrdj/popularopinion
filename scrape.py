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

tweets = tweepy.Cursor(api.search, q=queryTerm, lang="en").items(10)
totalCount = 0
totalNeg = 0
totalPos = 0
totalNeutral = 0
totalMixture = 0
for tweet in tweets:
    # print(tweet.text)
    totalCount += 1
    newTweet = tweet.text.encode('ascii', 'ignore')
    # print(sentiment_analyzer_scores(newTweet)['neg'])
    totalNeg += sentiment_analyzer_scores(newTweet)['neg']
    totalNeutral += sentiment_analyzer_scores(newTweet)['neu']
    totalPos += sentiment_analyzer_scores(newTweet)['pos']
    totalMixture += sentiment_analyzer_scores(newTweet)['compound']

# print(totalCount)
print(("Negative Opinions: " + totalNeg/totalCount)*100 + "%")
print(("Positive Opinions: " + totalPos/totalCount)*100 + "%")
print(("Neutral Opinions: " + totalNeutral/totalCount)*100 + "%")
print(("Mixed Opinions: " + totalMixture/totalCount)*100 + "%")
