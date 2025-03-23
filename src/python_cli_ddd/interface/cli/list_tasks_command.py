"""タスク一覧表示コマンド

このモジュールは、タスク一覧を表示するCLIコマンドを提供します。
"""

import click

from tabulate import tabulate

from python_cli_ddd.application.usecases.task.list_tasks_usecase import ListTasksUseCase
from python_cli_ddd.infrastructure.database.initialize import initialize_database
from python_cli_ddd.infrastructure.repositories.sqlite_task_repository import (
    SQLiteTaskRepository,
)


@click.command()
def main() -> None:
    """タスク一覧を表示する"""
    # データベースの初期化
    initialize_database()

    # リポジトリとユースケースの作成
    repository = SQLiteTaskRepository()
    usecase = ListTasksUseCase(repository)

    # タスク一覧の取得
    result = usecase.execute()

    # 結果の表示
    if not result.tasks:
        click.echo("タスクがありません。")
        return

    # タスク一覧をテーブル形式で表示
    headers = ["ID", "タイトル", "説明", "作成日時", "完了"]
    table = [
        [
            task.id,
            task.title,
            task.description or "",
            task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "✓" if task.completed else "",
        ]
        for task in result.tasks
    ]
    click.echo(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
