from client.twitter_client import Twitter_Client
from queue import Queue
import time

a = None

def main(query, limit, q:Queue, interval = 10):
    #interval is assumed to be minutes
    global a
    while True:
        if a is None:
            temp_a = 0
        else:
            temp_a = a
        tc = Twitter_Client()
        tweets = tc.get_tweet(query=query, limit=limit, since_id=a)
        for tweet in tweets:
            if tweet.id > temp_a:
                temp_a = tweet.id
            q.put(tweet)
        a = temp_a
        time.sleep((interval*60))

if __name__ == "__main__":
    q = Queue(maxsize=0)
    main(
        query="@Everbridge (-from:Everbridge) (-from:EBHealthcare)",
        limit=100,
        q=q,
        interval=10
    )