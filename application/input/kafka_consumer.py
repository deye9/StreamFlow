from kafka import KafkaConsumer
from domain.models.tweet import Tweet
from domain.services.tweet_service import TweetService

class KafkaTweetConsumer:
    def __init__(self, topic: str, bootstrap_servers: str):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        )

    def consume(self):
        for message in self.consumer:
            tweet_data = message.value
            tweet = Tweet(
                text=TweetService.clean_text(tweet_data["text"]),
                created_at=tweet_data["created_at"],
                user=tweet_data["user"]["screen_name"],
            )
            yield tweet
