"""タスクリポジトリのインターフェース

このモジュールは、タスク管理のためのリポジトリインターフェースを定義します。
"""

from abc import ABC, abstractmethod

from python_cli_ddd.domain.models.task import Task


class TaskRepository(ABC):
    """タスクリポジトリのインターフェース"""

    @abstractmethod
    def find_all(self) -> list[Task]:
        """全てのタスクを取得する

        Returns:
            タスクのリスト
        """
        pass

    @abstractmethod
    def find_by_id(self, task_id: int) -> Task | None:
        """IDによってタスクを取得する"""
        pass

    @abstractmethod
    def save(self, task: Task) -> None:
        """タスクを保存する

        Args:
            task: 保存するタスク
        """
        pass

    @abstractmethod
    def delete(self, task_id: int) -> None:
        """タスクを削除する"""
        pass
