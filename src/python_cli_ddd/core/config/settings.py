"""アプリケーション設定モジュール

このモジュールは、アプリケーション全体の設定を管理します。
環境変数やconfigファイルからの設定読み込みを担当します。
"""

import os

from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from .interfaces import ConfigInterface


class Settings(ConfigInterface):
    """アプリケーション設定を管理するクラス"""

    def __init__(self) -> None:
        # プロジェクトのルートディレクトリを取得
        self.base_dir = Path(__file__).parent.parent.parent.parent.parent.resolve()

        # .envファイルをロード
        load_dotenv(self.base_dir / ".env")

        # 設定値を保持する辞書
        self._settings: dict[str, Any] = {
            # 基本設定
            "APP_ENV": os.getenv("APP_ENV", "development"),
            "DEBUG": os.getenv("DEBUG", "false").lower() == "true",
            # ログ設定
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "LOG_DIR": os.getenv("LOG_DIR", str(self.base_dir / "logs")),
            # データベース設定
            "DB_HOST": os.getenv("DB_HOST", "localhost"),
            "DB_PORT": int(os.getenv("DB_PORT", "5432")),
            "DB_NAME": os.getenv("DB_NAME", "mydatabase"),
            "DB_USER": os.getenv("DB_USER", "user"),
            "DB_PASSWORD": os.getenv("DB_PASSWORD", ""),
        }

    def get(self, key: str, default: Any = None) -> Any:
        """設定値を取得する"""
        return self._settings.get(key, default)

    def get_bool(self, key: str, default: bool = False) -> bool:
        """真偽値として設定値を取得する"""
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        return str(value).lower() == "true"

    def get_int(self, key: str, default: int = 0) -> int:
        """整数値として設定値を取得する"""
        value = self.get(key, default)
        return int(value)

    def get_str(self, key: str, default: str = "") -> str:
        """文字列として設定値を取得する"""
        value = self.get(key, default)
        return str(value)


# シングルトンインスタンスを作成
settings = Settings()
