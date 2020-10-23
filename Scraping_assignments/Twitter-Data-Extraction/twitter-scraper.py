#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

import tweepy

# Loading Twitter API Credentials

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

users = ["JoeBiden", "realDonaldTrump"]


def get_all_tweets(screen_name):
    # Access to only close to 3200 tweets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # An array to hold all the tweets
    all_the_tweets = []
    oldest_tweet = None
    new_tweets = [1]
    print("For "+ screen_name+" -")
    while len(new_tweets) > 0:
        # Fetch and save tweets in multiple of 200
        if oldest_tweet is None:
            new_tweets = api.user_timeline(screen_name=screen_name, count=200)
        else:
            new_tweets = api.user_timeline(screen_name=screen_name,
                                           count=200, max_id=oldest_tweet)

        all_the_tweets.extend(new_tweets)

        # Save id of oldest tweet
        oldest_tweet = all_the_tweets[-1].id - 1
        print('...%s tweets have been downloaded so far' % len(all_the_tweets))

    # transforming the tweets into a 2D array that will be used to populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.favorite_count,
                  tweet.retweet_count, tweet.text.encode('utf-8')] for tweet in all_the_tweets]

    # writing to the csv file
    with open(screen_name + '_tweets.csv', 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'created_at', 'favorite_count', 'retweet_count', 'text'])
        writer.writerows(outtweets)



for user in users:
    get_all_tweets(user)
