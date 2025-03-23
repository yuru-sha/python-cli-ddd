"""依存性注入コンテナモジュール

このモジュールは、アプリケーション全体の依存性注入を管理します。
アプリケーションの中核的なDI (Dependency Injection) 機能を提供します。
"""

from typing import cast

from dependency_injector import containers, providers

from python_cli_ddd.application.usecases.message.print_message_usecase import (
    PrintMessageUseCase,
)
from python_cli_ddd.core.config.interfaces import ConfigInterface
from python_cli_ddd.core.di.interfaces import DIContainer, UseCaseProvider
from python_cli_ddd.infrastructure.config.settings import Settings


class ApplicationContainer(containers.DeclarativeContainer, DIContainer):
    """アプリケーションの依存性注入コンテナ実装"""

    # Core Components
    _config: providers.Singleton[Settings] = providers.Singleton(Settings)

    # UseCases
    _print_message_usecase: providers.Factory[PrintMessageUseCase] = providers.Factory(
        PrintMessageUseCase,
    )

    @property
    def config(self) -> ConfigInterface:
        """設定プロバイダー"""
        return cast("ConfigInterface", self._config())

    @property
    def print_message_usecase(self) -> UseCaseProvider:
        """メッセージ出力ユースケースのプロバイダー"""
        return cast("UseCaseProvider", self._print_message_usecase)

    def init_resources(self) -> None:
        """コンテナのリソースを初期化する"""
        super().init_resources()

    # 追加のコンポーネント: repositories, services, use_cases
