class TweetService:
    @staticmethod
    def clean_text(text: str) -> str:
        return text.lower().strip()
