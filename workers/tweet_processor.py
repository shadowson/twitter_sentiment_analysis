from core.functions import Functions
from queue import Queue
from model.tweetlog import TweetRecord

def main(tweet_q:Queue, archive_q:Queue):
    helpers = Functions()
    while True:
        tweet = tweet_q.get(block=True, timeout=None)
        clean_tweet = helpers.clean_string(tweet.text)
        val = helpers.get_sentiment(clean_tweet=clean_tweet)
        tr = TweetRecord(tweet=tweet, sentiment=val)
        archive_q.put(tr)