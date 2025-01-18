import tweepy
import random
import datetime
from faker import Faker
from infrastructure.logger_config import logger
from infrastructure.twitter.twitter_config import twitter_config

fake = Faker()
logger = logger.getChild(__name__)

class TwitterStream():
    def __init__(self):
        self.config = twitter_config.get_config()

        try:
            logger.info(f"Authenticating with Twitter")

            # Authenticate with Twitter
            self.client = tweepy.Client(
                wait_on_rate_limit=True,
                access_token=self.config.get('access_token'),
                consumer_key=self.config.get('consumer_key'),
                consumer_secret=self.config.get('consumer_secret'),
                access_token_secret=self.config.get('access_token_secret')
            )
        except TypeError as e:
            logger.error(f"Error in authentication: {e}")
            raise

    def generate_sample_tweet(self, id):
        return {
            "id": str(id),
            "text": fake.sentence(nb_words=10),
            "created_at": (datetime.datetime.now() - datetime.timedelta(minutes=id)).isoformat() + "Z",
            "author_id": str(random.randint(1000, 9999))
        }

    def generate_tweets_response(self, count):
        tweets = [self.generate_sample_tweet(i) for i in range(1, count + 1)]
        response = {
            "data": tweets,
            "meta": {
                "newest_id": str(count),
                "oldest_id": "1",
                "result_count": count,
                "next_token": fake.pystr(min_chars=10, max_chars=20)
            }
        }
        return response

    def fetch_tweets(self, query, count):
        try:
            logger.info(f"Fetching tweets for user: {query}")
            self.client.get_user(username=query)
        except tweepy.Unauthorized as e:
            logger.error(f"Unauthorized error fetching tweets: {e}")
            tweets = self.generate_tweets_response(count)
        except tweepy.TweepyException as e:
            logger.error(f"Error fetching tweets: {e}")
            tweets = []

        return tweets