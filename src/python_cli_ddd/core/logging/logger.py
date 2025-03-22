
from ...core.config.interfaces import ConfigInterface
from ...infrastructure.config.settings import settings
from ...infrastructure.logging.handlers import DefaultLogger
from .interfaces import LoggerInterface


class LoggerFactory:
    """ロガーのファクトリクラス"""

    _instance: LoggerInterface | None = None

    @classmethod
    def get_logger(cls, config: ConfigInterface | None = None) -> LoggerInterface:
        """ロガーのインスタンスを取得する"""
        if cls._instance is None:
            if config is None:
                config = settings
            cls._instance = DefaultLogger(config)
        return cls._instance

    @classmethod
    def reset(cls) -> None:
        """ロガーのインスタンスをリセットする（主にテスト用）"""
        cls._instance = None


# 簡単にアクセスできるようにするためのショートカット
logger = LoggerFactory.get_logger()
