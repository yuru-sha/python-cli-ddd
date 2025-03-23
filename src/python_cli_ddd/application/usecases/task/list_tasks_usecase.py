"""タスク一覧取得のユースケース

このモジュールは、タスク一覧を取得するユースケースを定義します。
"""

from dataclasses import dataclass
from datetime import datetime

from python_cli_ddd.domain.repositories.task_repository import TaskRepository


@dataclass
class TaskDTO:
    """タスクのデータ転送オブジェクト"""

    id: int | None
    title: str
    description: str | None
    created_at: datetime
    completed: bool


@dataclass
class ListTasksOutput:
    """タスク一覧取得の出力値オブジェクト"""

    tasks: list[TaskDTO]


class ListTasksUseCase:
    """タスク一覧を取得するユースケース"""

    def __init__(self, task_repository: TaskRepository) -> None:
        self._task_repository = task_repository

    def execute(self) -> ListTasksOutput:
        """ユースケースを実行する"""
        tasks = self._task_repository.find_all()
        return ListTasksOutput(
            tasks=[
                TaskDTO(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    created_at=task.created_at,
                    completed=task.completed,
                )
                for task in tasks
            ]
        )
