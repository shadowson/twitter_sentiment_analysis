import re
from textblob import TextBlob
from core.ref.ref_enums import Sentiment

class Functions:
    def __init__(self):
        self.ref_sentiment = Sentiment
    #generic
    def clean_string(self, string):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", string).split())

    #twitter client specific
    def get_sentiment(self, clean_tweet):
        #this function expects the tweet text to be cleared of non text data such as hyperlinks and special chars
        #if you are getting unexpected errors check to ensure that you are running the above "clean_string" on the
        #tweet prior to sentiment processing
        tb = TextBlob(clean_tweet)
        if tb.polarity > 0:
            return self.ref_sentiment.POSITIVE
        elif tb.polarity == 0:
            return self.ref_sentiment.NUETRAL
        else:
            return self.ref_sentiment.NEGATIVE

