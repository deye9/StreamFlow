from dotenv import load_dotenv
import os

# Read the ES_HOST and ES_INDEX environment variables from the .env file
# and return them as a dictionary

def get_es_config():
    
    # Load environment variables from .env file
    load_dotenv()

    # Read values from environment variables
    return {
        'host': os.getenv('ES_HOST'),
        'index': os.getenv('ES_INDEX')
    }