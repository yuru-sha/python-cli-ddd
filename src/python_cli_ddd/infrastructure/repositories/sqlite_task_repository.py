"""SQLiteを使用したタスクリポジトリの実装

このモジュールは、SQLiteを使用したタスクリポジトリの具体的な実装を提供します。
"""

from datetime import datetime

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from python_cli_ddd.domain.models.task import Task
from python_cli_ddd.domain.repositories.task_repository import TaskRepository
from python_cli_ddd.infrastructure.database.models import TaskModel
from python_cli_ddd.infrastructure.database.settings import DATABASE_URL


class SQLiteTaskRepository(TaskRepository):
    """SQLiteを使用したタスクリポジトリの実装"""

    def __init__(self) -> None:
        self.engine = create_engine(DATABASE_URL)

    def find_all(self) -> list[Task]:
        """すべてのタスクを取得する"""
        with Session(self.engine) as session:
            stmt = select(TaskModel)
            result = session.execute(stmt)
            return [
                Task(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    created_at=datetime.fromisoformat(task.created_at),
                    completed=task.completed,
                )
                for task in result.scalars()
            ]

    def find_by_id(self, task_id: int) -> Task | None:
        """IDによってタスクを取得する"""
        with Session(self.engine) as session:
            stmt = select(TaskModel).where(TaskModel.id == task_id)
            result = session.execute(stmt)
            task = result.scalar_one_or_none()
            if task is None:
                return None
            return Task(
                id=task.id,
                title=task.title,
                description=task.description,
                created_at=datetime.fromisoformat(task.created_at),
                completed=task.completed,
            )

    def save(self, task: Task) -> None:
        """タスクを保存する"""
        with Session(self.engine) as session:
            task_model = TaskModel(
                id=task.id,
                title=task.title,
                description=task.description,
                created_at=task.created_at,
                completed=task.completed,
            )
            session.merge(task_model)
            session.commit()

    def delete(self, task_id: int) -> None:
        """タスクを削除する"""
        with Session(self.engine) as session:
            stmt = select(TaskModel).where(TaskModel.id == task_id)
            task = session.execute(stmt).scalar_one_or_none()
            if task:
                session.delete(task)
                session.commit()
