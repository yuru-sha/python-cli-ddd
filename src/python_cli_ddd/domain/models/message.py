from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    content: str
    created_at: datetime

    @classmethod
    def create(cls, content: str) -> "Message":
        return cls(content=content, created_at=datetime.now())
