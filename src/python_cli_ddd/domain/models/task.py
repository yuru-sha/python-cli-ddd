"""タスクのドメインモデル

このモジュールは、タスク管理のためのドメインモデルを定義します。
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """タスクを表すドメインモデル"""

    id: int | None
    title: str
    description: str | None
    created_at: datetime
    completed: bool

    @classmethod
    def create(cls, title: str, description: str | None = None) -> "Task":
        """新しいタスクを作成する"""
        return cls(
            id=None,
            title=title,
            description=description,
            created_at=datetime.now(),
            completed=False,
        )
