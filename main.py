import time
from infrastructure.logger_config import logger
from domain.services.tweet_service import TwitterStream
from infrastructure.kafka.kafka_producer import KafkaProducerClient

logger = logger.getChild(__name__)

def main():
    """
    Main function to consume tweets from Kafka and index them into Elasticsearch.
    """
    total_tweets = 0
    batch_size = 100
    tweets_batch = []
    start_time = time.time()

    twitter_stream = TwitterStream()
    tweets = twitter_stream.fetch_tweets(query="QUERY", count=100)

    producer = KafkaProducerClient()
    producer.send_message(tweets)
    producer.close()

if __name__ == "__main__":
    main()
