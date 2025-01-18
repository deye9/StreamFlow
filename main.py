import logging
import time
from application.input.kafka_consumer import KafkaTweetConsumer
from application.output.elasticsearch_client import ElasticsearchClient
from infrastructure.kafka.kafka_config import kafka_config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    Main function to consume tweets from Kafka and index them into Elasticsearch.
    """
    total_tweets = 0
    batch_size = 100
    tweets_batch = []
    start_time = time.time()
    kafka_settings = kafka_config.get_config()
    kafka_consumer = KafkaTweetConsumer(topic=kafka_settings.get('topic'), bootstrap_servers=kafka_settings.get('broker_url'))
    es_client = ElasticsearchClient()

    try:
        with kafka_consumer as consumer:
            for tweet in consumer.consume():
                tweets_batch.append(tweet.__dict__)
                total_tweets += 1
                if len(tweets_batch) >= batch_size:
                    es_client.bulk_index(index="tweets", tweets=tweets_batch)
                    tweets_batch.clear()
                # Index any remaining tweets in the batch
                if tweets_batch:
                    es_client.bulk_index(index="tweets", tweets=tweets_batch)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        throughput = total_tweets / elapsed_time
        logger.info(f"Total tweets processed: {total_tweets}")
        logger.info(f"Total time taken: {elapsed_time:.2f} seconds")
        logger.info(f"Throughput: {throughput:.2f} tweets/second")

if __name__ == "__main__":
    main()
