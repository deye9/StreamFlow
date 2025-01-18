from dotenv import load_dotenv
import os

# Read the TOPIC_NAME and KAFKA_BROKER_URL environment variables from the .env file
# and return them as a dictionary

def get_kafka_config():

    # Load environment variables from .env file
    load_dotenv()

    # Read values from environment variables
    return {
        'topic': os.getenv('TOPIC_NAME'),
        'broker_url': os.getenv('KAFKA_BROKER_URL')
    }

