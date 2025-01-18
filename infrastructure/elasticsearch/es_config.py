from dotenv import load_dotenv
import os

class ESConfig:
    def __init__(self):
        load_dotenv()
        self.host = os.environ.get('es_host')
        self.index = os.environ.get('es_index')

    def get_config(self):
        return {
            'host': self.host,
            'index': self.index
        }

es_config = ESConfig()