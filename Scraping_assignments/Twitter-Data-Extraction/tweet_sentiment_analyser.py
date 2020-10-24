#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textblob import TextBlob

stats = {
    "trump": {
        "neutral": 0,
        "positive": 0,
        "negative": 0
    },
    "biden": {
        "neutral": 0,
        "positive": 0,
        "negative": 0
    }
}


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    # analyse text using TextBlob
    analysis = TextBlob(clean_tweet(tweet))

    # Select positive negative or neutral sentiment
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


def update_stats(candidate, data, stats, counter):
    for index, tweet in enumerate(data):
        if index == counter:
            break
        sentiment = get_tweet_sentiment(tweet['tweetText'])
        if sentiment == 0:
            stats[candidate]["neutral"] += 1
        elif sentiment > 0:
            stats[candidate]["positive"] += 1
        else:
            stats[candidate]["negative"] += 1
    return stats


trump_data = pd.read_csv("realDonaldTrump_tweets.csv")
biden_data = pd.read_csv("JoeBiden_tweets.csv")

with open('trump.json') as f: trump_sentiment_data = json.load(f)
with open('biden.json') as g: biden_sentiment_data = json.load(g)

counter = min(len(trump_sentiment_data), len(biden_sentiment_data))

stats = update_stats("trump", trump_sentiment_data, stats, counter)
stats = update_stats("biden", biden_sentiment_data, stats, counter)

# Create the labels and data set for creating the bar graph
labels = ['Neutral', 'Positive', 'Negative', "Favorite Count", "Retweet Count"]
trump_data = [int(stats["trump"]["neutral"]) , int(stats["trump"]["positive"]) ,int(stats["trump"]["negative"]) ,
              int(trump_data["favorite_count"].mean()//100), int(trump_data["retweet_count"].mean()//100)]
biden_data = [int(stats["biden"]["neutral"]) , int(stats["biden"]["positive"]) , int(stats["biden"]["negative"]) ,
              int(biden_data["favorite_count"].mean()//100), int(biden_data["retweet_count"].mean()//100)]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, trump_data, width, label='Trump')
rects2 = ax.bar(x + width / 2, biden_data, width, label='Biden')

# Set x and y axis titles
ax.set_ylabel('Number of Tweets')
ax.set_title('Sentiment of Tweets')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()
plt.show()
