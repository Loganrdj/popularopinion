import os
import tweepy
import config
import csv
import json
import pandas
import unicodedata
from progress.bar import Bar
# from pandas import DataFrame
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
queryTerm = input("What would you like to search for? ")
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

tweets = tweepy.Cursor(api.search, q=queryTerm, lang="en").items(30)
totalCount = 0
totalNeg = 0
totalPos = 0
totalNeutral = 0
totalMixture = 0
totalUnknown = 0

print("Please wait a moment!")
bar = Bar('Analyzing', max=30)

for tweet in tweets:
    print(tweet.text)
    totalCount += 1.0
    newTweet = tweet.text.encode('ascii', 'ignore')
    # print(sentiment_analyzer_scores(newTweet))
    score = sentiment_analyzer_scores(str(newTweet))
    if(score['neg'] > score['pos']):
        totalNeg = totalNeg + 1.0
    elif(score['pos'] > score['neg']):
        totalPos = totalPos + 1.0
    else:
        totalUnknown += 1.0
    bar.next()

bar.finish()
# print(totalCount)
# print(totalNeg)
# print(totalPos)
# print(totalUnknown)
resultPos = totalPos/totalCount * 100.0
resultNeg = totalNeg/totalCount * 100.0
resultUnknown = totalUnknown/totalCount * 100.0

print(f'Out of {int(totalCount)} tweets and opinions,')
print(f'Negative Opinions: {resultNeg}%')
print(f'Positive Opinions: {resultPos}%')
print(f'Neutral Opinions: {resultUnknown}%')
