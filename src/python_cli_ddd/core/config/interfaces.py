"""設定インターフェースモジュール

このモジュールは、設定管理のための抽象インターフェースを定義します。
"""

from abc import ABC, abstractmethod
from typing import Any


class ConfigInterface(ABC):
    """設定管理のための抽象インターフェース"""

    @abstractmethod
    def get(self, key: str, default: Any = None) -> Any:
        """設定値を取得する"""
        pass

    @abstractmethod
    def get_bool(self, key: str, default: bool = False) -> bool:
        """真偽値として設定値を取得する"""
        pass

    @abstractmethod
    def get_int(self, key: str, default: int = 0) -> int:
        """整数値として設定値を取得する"""
        pass

    @abstractmethod
    def get_str(self, key: str, default: str = "") -> str:
        """文字列として設定値を取得する"""
        pass
