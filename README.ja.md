# python-cli-ddd

[![CI](https://github.com/yuru-sha/python-cli-ddd/actions/workflows/ci.yml/badge.svg)](https://github.com/yuru-sha/python-cli-ddd/actions/workflows/ci.yml)

ドメイン駆動設計（DDD）とクリーンアーキテクチャの原則を実践するPythonのCLIアプリケーション。

## 機能

- CLIコマンドによるタスク管理
- SQLiteデータベースによるデータ永続化
- クリーンアーキテクチャとDDDの原則に基づく設計
- `dependency-injector`を使用した依存性注入
- 型ヒントと厳密な型チェック
- `ruff`と`mypy`による包括的なリンティング

## 必要条件

- Python 3.12以上
- 依存関係管理にPoetryまたはpipを使用

## インストール

```bash
# リポジトリのクローン
git clone https://github.com/yuru-sha/python-cli-ddd.git
cd python-cli-ddd

# 依存関係のインストール
pip install -e .
```

## 利用可能なコマンド

### タスク一覧
フォーマットされた表でタスクを表示します：
```bash
list-tasks
```

### メッセージ表示
デバッグ情報を含むメッセージを表示します：
```bash
print-message "メッセージ"
```

## 開発

### 開発環境のセットアップ

```bash
# 開発用依存関係のインストール
pip install -e ".[dev]"
```

### テストの実行

```bash
make test
```

### リンティング

```bash
make lint
```

## プロジェクト構造

```
src/python_cli_ddd/
├── domain/           # ドメイン層（エンティティ、リポジトリ）
├── application/      # アプリケーション層（ユースケース）
├── infrastructure/   # インフラストラクチャ層（データベース、外部サービス）
└── interface/        # インターフェース層（CLIコマンド）
```

## ライセンス

MITライセンス