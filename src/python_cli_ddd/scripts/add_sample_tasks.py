"""サンプルタスク追加スクリプト

このスクリプトは、開発用のサンプルタスクをデータベースに追加します。
"""

from python_cli_ddd.domain.models.task import Task
from python_cli_ddd.infrastructure.database.initialize import initialize_database
from python_cli_ddd.infrastructure.repositories.sqlite_task_repository import (
    SQLiteTaskRepository,
)


def main() -> None:
    """サンプルタスクを追加する"""
    # データベースの初期化
    initialize_database()

    # リポジトリの作成
    repository = SQLiteTaskRepository()

    # サンプルタスクの作成と保存
    tasks = [
        Task.create(
            title="プロジェクトの設計書作成",
            description="新規プロジェクトの基本設計書を作成する。要件定義から始める。",
        ),
        Task.create(
            title="週次ミーティングの準備",
            description="アジェンダの作成と資料の準備を行う。",
        ),
        Task.create(
            title="バグ修正 #123",
            description="ログイン画面でパスワードリセットが動作しない問題の修正。",
        ),
        Task.create(
            title="新機能の実装",
            description="ユーザープロフィール編集機能の追加。写真アップロード機能を含む。",
        ),
        Task.create(
            title="テストコードの作成",
            description="新しく追加した機能のユニットテストとE2Eテストを作成する。",
        ),
    ]

    for task in tasks:
        repository.save(task)


if __name__ == "__main__":
    main()
