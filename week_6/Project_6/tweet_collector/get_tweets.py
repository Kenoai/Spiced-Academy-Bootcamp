import tweepy
import os
import pymongo
import logging
from datetime import datetime
from datetime import timezone    


client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twitter

##################
# Authentication #
##################
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)

#####################
# Search for Tweets #
#####################

# https://docs.tweepy.org/en/stable/client.html#tweepy.Client.search_recent_tweets
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
tweet_data = {}
# - means NOT
search_query = "#aiart -is:retweet -is:reply -is:quote lang:en has:media"

"""tweets = client.search_recent_tweets(query=search_query, tweet_fields=['created_at'], expansions='attachments.media_keys',media_fields=['url'],max_results=100)

"""

"""for tweet in tweets.data:
    attachments = tweet.data['attachments']
    media_keys = attachments['media_keys']
    tweet_data['tweet'] = tweet['text']
    tweet_data['created_at'] = tweet['created_at']
    #logging.critical("TEXT: " + tweet.text)
    #if media[media_keys[0]].url:
    #    logging.critical("IMAGE" + media[media_keys[0]].url)
    #logging.critical("DICT TWEET" + str(dict(tweet)))
    #logging.critical(media[media_keys[0]].url)
    if media[media_keys][0]:
        tweet_data['image'] = media[media_keys][0].url
    logging.critical(tweet_data)
    #db.tweets.insert_one(dict(tweet_data))"""


#last working

cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['created_at'],
    expansions=['attachments.media_keys'],
    media_fields=['url'],
    max_results=10
)

# Get list of media from the includes object
#media = {m["media_key"]: m for m in tweets.includes['media']}

for tweet in cursor:
    tweet_data = {}
    #logging.critical("DATA " + str(tweet.data))
    logging.critical("INCLUDES:")
    if tweet.includes:
        url = tweet.includes['media'][0].url
    else:
        pass
    #logging.critical(url)
    #tweet = dict(tweet)
    tweet_data['created_at'] = tweet.data[0]['created_at']

    # dtime = tweet['created_at']
    #new_datetime = datetime.strftime(datetime.strptime(tweet_data['created_at'],'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d %H:%M:%S')



    logging.critical(tweet_data['created_at'])
    tweet_data['text'] = tweet.data[0]['text']
    tweet_data['image'] = url
    logging.critical(tweet_data)
    #logging.critical("data: " + str(tweet.data))
    db.tweets.insert_one(dict(tweet_data))
    #print(tweet.attachments)

"""for tweet in tweets.data:
    attachments = tweet['attachments']
    media_keys = attachments['media_keys']
    if media[media_keys[0]].url:
        tweet_data['image'] = media[media_keys[0]].url
    logging.critical("data: " + str(tweet.data))

"""
