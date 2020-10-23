import json

import tweepy

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_token = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']

# Authenticate twitter Api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_terms = ["trump", "biden"]

for term in search_terms:
    # create a tweepy cursor
    c = tweepy.Cursor(api.search, q='%' + term)
    c.pages(100)  # number of pages of tweets you want to fetch

    # Save the tweets
    tweetJson = []
    for tweet in c.items():
        if tweet.lang == 'en':
            createdAt = str(tweet.created_at)
            authorCreatedAt = str(tweet.author.created_at)
            tweetJson.append(
                {'tweetText': tweet.text,
                 'tweetCreatedAt': createdAt,
                 'authorName': tweet.author.name,
                 })

    # dump the data into json format
    out_file = open(term + ".json", "w")
    json.dump(tweetJson, out_file, indent=6)
    out_file.close()
