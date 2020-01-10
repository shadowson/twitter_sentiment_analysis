import json
from core.ref.ref_enums import Sentiment

class TweetRecord:
    def __init__(self, tweet, sentiment):
        self.tweetId = tweet.id
        self.tweetText = tweet.text
        self.sentiment = sentiment
        self.created = tweet.created_at
        self.authorId = tweet.author.id
        self.authorName = tweet.author.name
        self.authorFollowersCount = tweet.author.followers_count
        self.isRetweeted = tweet.retweeted
        self.retweetCount = tweet.retweet_count

    def serialize(self):
        record = {
            "tweetId": self.tweetId,
            "tweetText": self.tweetText,
            "sentiment": self.sentiment.value,
            "created": self.created.isoformat(),
            "authorId": self.authorId,
            "authorName": self.authorName,
            "authorFollowersCount": self.authorFollowersCount,
            "isRetweeted": self.isRetweeted,
            "retweetCount": self.retweetCount
        }
        return record
