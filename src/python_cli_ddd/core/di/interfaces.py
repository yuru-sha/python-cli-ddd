"""依存性注入コンテナのインターフェース定義

このモジュールは、依存性注入コンテナの抽象インターフェースを定義します。
アプリケーション層はこのインターフェースに依存します。
"""

from abc import ABC, abstractmethod
from typing import Protocol

from python_cli_ddd.core.config.interfaces import ConfigInterface


class UseCaseProvider(Protocol):
    """ユースケースのプロバイダーインターフェース"""

    def __call__(self) -> "PrintMessageUseCase":  # type: ignore
        """ユースケースのインスタンスを提供する"""
        ...


class DIContainer(ABC):
    """依存性注入コンテナの抽象インターフェース"""

    @property
    @abstractmethod
    def config(self) -> ConfigInterface:
        """設定プロバイダー"""
        pass

    @property
    @abstractmethod
    def print_message_usecase(self) -> UseCaseProvider:
        """メッセージ出力ユースケースのプロバイダー"""
        pass

    @abstractmethod
    def init_resources(self) -> None:
        """コンテナのリソースを初期化する"""
        pass
