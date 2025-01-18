import json
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError
from infrastructure.logger_config import logger
from infrastructure.kafka.kafka_config import kafka_config

logger = logger.getChild(__name__)

class KafkaProducerClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(KafkaProducerClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            config = kafka_config.get_config()
            logger.info(f"Kafka producer initializing")

            self.producer = KafkaProducer(
                bootstrap_servers=config['broker_url'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            )
            logger.info(f"Kafka producer created")
            self.topic = config['topic']
            self.initialized = True

    def send_message(self, message):
        try:
            logger.info(f"Sending message(s) to topic {self.topic}")
            self.producer.send(self.topic, value=message)
            
            logger.info(f"Message(s) sent to topic {self.topic}")
            self.producer.flush()
        except KafkaTimeoutError as e:
            logger.error(f"Failed to send message(s): KafkaTimeoutError: {e}")
        except Exception as e:
            logger.error(f"Failed to send message(s): {e}")

    def close(self):
        logger.info(f"Closing Kafka producer")
        self.producer.close()
