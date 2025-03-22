import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from ..config.settings import settings


class Logger:
    """アプリケーションのロギングを管理するクラス"""

    def __init__(self) -> None:
        self.logger = logging.getLogger("python_cli_ddd")

        # 既存のハンドラーをクリア
        self.logger.handlers.clear()

        # ログレベルの設定
        log_level = getattr(logging, settings.LOG_LEVEL, logging.INFO)
        self.logger.setLevel(log_level)

        # フォーマッターの作成
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # コンソールハンドラーの設定
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # ファイルハンドラーの設定（設定されている場合）
        if hasattr(settings, "LOG_DIR"):
            log_dir = Path(settings.LOG_DIR)
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


# シングルトンインスタンスを作成
logger = Logger()
