from application.input.kafka_consumer import KafkaTweetConsumer
from application.output.elasticsearch_client import ElasticsearchClient
from infrastructure.kafka.kafka_config import get_kafka_config

def main():
    """
    Main function to consume tweets from Kafka and index them into Elasticsearch.
    """
    config = get_kafka_config()
    kafka_consumer = KafkaTweetConsumer(topic=config.get('topic'), bootstrap_servers=config.get('broker_url'))
    es_client = ElasticsearchClient()
    batch_size = 100
    tweets_batch = []

    try:
        with kafka_consumer as consumer:
            for tweet in consumer.consume():
                tweets_batch.append(tweet.__dict__)
                if len(tweets_batch) >= batch_size:
                    es_client.bulk_index(index="tweets", tweets=tweets_batch)
                    tweets_batch.clear()
            # Index any remaining tweets in the batch
            if tweets_batch:
                es_client.bulk_index(index="tweets", tweets=tweets_batch)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
