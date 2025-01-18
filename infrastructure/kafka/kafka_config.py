from dotenv import load_dotenv
import os

class KafkaConfig:
    def __init__(self):
        load_dotenv()
        self.topic_name = os.environ.get('TOPIC_NAME')
        self.broker_url = os.environ.get('KAFKA_BROKER_URL')

    def get_config(self):
        return {
            'topic': self.topic_name,
            'broker_url': self.broker_url
        }

kafka_config = KafkaConfig()