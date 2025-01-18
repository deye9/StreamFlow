from dataclasses import dataclass

@dataclass
class Tweet:
    text: str
    created_at: str
    user: str
