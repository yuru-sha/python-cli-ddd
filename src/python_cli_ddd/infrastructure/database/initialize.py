"""データベース初期化

このモジュールは、データベースの初期化を行います。
"""

from sqlalchemy import create_engine

from .models import Base
from .settings import DATABASE_URL


def initialize_database() -> None:
    """データベースを初期化する"""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
