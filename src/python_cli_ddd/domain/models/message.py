from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    content: str
    created_at: datetime

    @classmethod
    def create(cls, content: str) -> "Message":
        return cls(content=content, created_at=datetime.now())

    def format_message(self) -> str:
        """メッセージを整形して返す"""
        return self.content

    @property
    def timestamp(self) -> datetime:
        """タイムスタンプを返す"""
        return self.created_at
