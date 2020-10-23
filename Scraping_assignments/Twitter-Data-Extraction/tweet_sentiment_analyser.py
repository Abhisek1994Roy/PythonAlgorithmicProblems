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


biden_data = pd.read_csv("JoeBiden_tweets.csv")
trump_data = pd.read_csv("realDonaldTrump_tweets.csv")

with open('trump.json') as f: trump_sentiment_data = json.load(f)
with open('biden.json') as g: biden_sentiment_data = json.load(g)

counter = min(len(trump_sentiment_data), len(biden_sentiment_data))

stats = update_stats("trump", trump_sentiment_data, stats, counter)
stats = update_stats("biden", biden_sentiment_data, stats, counter)

# Create the labels and data set for creating the bar graph
labels = ['Neutral', 'Positive', 'Negative', "Favorite Count", "Retweet Count"]
trump_data = [stats["trump"]["neutral"] * 100, stats["trump"]["positive"] * 100, stats["trump"]["negative"] * 100,
              round(trump_data["favorite_count"].mean()), round(trump_data["retweet_count"].mean())]
biden_data = [stats["biden"]["neutral"] * 100, stats["biden"]["positive"] * 100, stats["biden"]["negative"] * 100,
              round(biden_data["favorite_count"].mean()), round(biden_data["retweet_count"].mean())]

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


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()
