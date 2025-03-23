import logging
import sys

from logging.handlers import RotatingFileHandler
from pathlib import Path

from python_cli_ddd.core.config.interfaces import ConfigInterface
from python_cli_ddd.core.logging.interfaces import LoggerInterface


class DefaultLogger(LoggerInterface):
    """デフォルトのロガー実装"""

    def __init__(self, config: ConfigInterface) -> None:
        self.logger = logging.getLogger("python_cli_ddd")
        self.logger.handlers.clear()

        # ログレベルの設定
        log_level = getattr(logging, config.get_str("LOG_LEVEL", "INFO"), logging.INFO)
        self.logger.setLevel(log_level)

        # フォーマッターの作成
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # コンソールハンドラーの設定
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # ファイルハンドラーの設定
        log_dir = Path(config.get_str("LOG_DIR", str(Path.cwd() / "logs")))
        log_dir.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_dir / "app.log",
            maxBytes=1024 * 1024,  # 1MB
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)
