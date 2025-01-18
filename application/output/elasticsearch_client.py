from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read values from environment variables
bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')

class ElasticsearchClient:
    def __init__(self, host="http://{bootstrap_servers}"):
        self.client = Elasticsearch(hosts=[host])

    def index_tweet(self, index: str, tweet: dict):
        self.client.index(index=index, body=tweet)
