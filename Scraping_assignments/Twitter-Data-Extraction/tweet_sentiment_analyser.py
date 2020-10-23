import pandas as pd
from textblob import TextBlob
import re
import numpy as np
import matplotlib.pyplot as plt

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
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1

def update_stats(candidate, data, stats):
    for ind in data.index:
        sentiment = get_tweet_sentiment(data['text'][ind])
        if sentiment == 0:
            stats[candidate]["neutral"] += 1
        elif sentiment > 0:
            stats[candidate]["positive"] += 1
        else:
            stats[candidate]["negative"] += 1
    return stats

biden_data = pd.read_csv("JoeBiden_tweets.csv")
trump_data = pd.read_csv("realDonaldTrump_tweets.csv")

stats = update_stats("trump", trump_data, stats)
stats = update_stats("biden", biden_data, stats)

# Create a graph of sentiments of both candidates
labels = ['Neutral', 'Positive', 'Negative']
trump_data = [stats["trump"]["neutral"],stats["trump"]["positive"],stats["trump"]["negative"]]
biden_data = [stats["biden"]["neutral"],stats["biden"]["positive"],stats["biden"]["negative"]]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, trump_data, width, label='Trump')
rects2 = ax.bar(x + width/2, biden_data, width, label='Biden')

# Add some text for labels, title and custom x-axis tick labels, etc.
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
