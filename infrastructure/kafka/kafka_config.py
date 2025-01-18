import os
from dotenv import load_dotenv

class KafkaConfig:
    def __init__(self):
        load_dotenv()
        self.topic_name = os.environ.get('topic_name')
        self.broker_url = os.environ.get('kafka_broker_url')

    def get_config(self):
        return {
            'topic': self.topic_name,
            'broker_url': self.broker_url
        }

kafka_config = KafkaConfig()