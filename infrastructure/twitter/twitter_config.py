import os
from dotenv import load_dotenv
from infrastructure.logger_config import logger

logger = logger.getChild(__name__)

class TwitterConfig:
    def __init__(self):
        load_dotenv()
        self.consumer_key = os.environ.get('consumer_key')
        self.access_token = os.environ.get('access_token')
        self.consumer_secret = os.environ.get('consumer_secret')
        self.access_token_secret = os.environ.get('access_token_secret')
        logger.info(f"Fetching Twitter config from environment variables")

    def get_config(self):
        return {
            'consumer_key': self.consumer_key,
            'access_token': self.access_token,
            'consumer_secret': self.consumer_secret,
            'access_token_secret': self.access_token_secret
        }

twitter_config = TwitterConfig()