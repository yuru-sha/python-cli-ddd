"""SQLAlchemyのモデル定義

このモジュールは、SQLAlchemyを使用したデータベースモデルを定義します。
"""

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """ベースモデル"""

    pass


class TaskModel(Base):
    """タスクのデータベースモデル"""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[str] = mapped_column(String(30), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
