from python_cli_ddd.core.logging.interfaces import LoggerInterface
from python_cli_ddd.infrastructure.config.settings import settings
from python_cli_ddd.infrastructure.logging.handlers import DefaultLogger


class Logger:
    """アプリケーションのロガーファクトリー"""

    _instance: LoggerInterface | None = None

    @classmethod
    def get_logger(cls) -> LoggerInterface:
        """ロガーのインスタンスを取得する"""
        if cls._instance is None:
            cls._instance = DefaultLogger(settings)
        return cls._instance

    @classmethod
    def reset(cls) -> None:
        """ロガーのインスタンスをリセットする (主にテスト用)"""
        cls._instance = None


# 簡単にアクセスできるようにするためのショートカット
logger = Logger.get_logger()
