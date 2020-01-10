import tweepy
from tweepy import OAuthHandler
from core.config.config import Config
from core.functions import Functions


class Twitter_Client:
    def __init__(self):
        #pull in all config info including keys
        self.config = Config()
        self.helpers = Functions()
        #try to creat a session
        try:
            self.auth = OAuthHandler(self.config.consumerkey, self.config.consumerkey_secret)
            self.auth.set_access_token(self.config.accesstoken, self.config.accesstoken_secret)
            self.client = tweepy.API(auth_handler=self.auth)
        except Exception as err:
            print("Authentication Failure")

    def get_tweet(self, query, limit, since_id=None):
        if since_id is None:
            return self.client.search(q=query, count=limit)
        else:
            return self.client.search(q=query, count=limit, since_id=since_id)

if __name__ == "__main__":
    tc = Twitter_Client()
    tweets = tc.get_tweet(query="@Everbridge (-from:Everbridge) (-from:EBHealthcare)", limit=10, since_id=0)
    for tweet in tweets:
        clean_tweet = tc.helpers.clean_string(tweet.text)
        val = tc.helpers.get_sentiment(clean_tweet=clean_tweet)
    print('YAY')