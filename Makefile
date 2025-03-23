.PHONY: help clean setup setup-dev lint format
.DEFAULT_GOAL := help

help: ## コマンド一覧を表示
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

clean: ## 一時ファイル、キャッシュ、ビルドアーティファクトを削除
	@echo "🧹 Cleaning project..."
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf .import_linter_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".DS_Store" -delete
	@echo "✨ Cleaned!"

setup: ## 本番環境用の依存関係をインストール
	@echo "📦 Installing production dependencies..."
	uv pip install .
	@echo "✅ Installation complete!"

setup-dev: ## 開発環境用の依存関係をインストール
	@echo "🔧 Installing development dependencies..."
	uv pip install -e ".[dev]"
	@echo "✅ Development setup complete!"

lint: ## コードの静的解析を実行（ruff, mypy）
	@echo "🔍 Running linters..."
	uv run ruff check --statistics src
	uv run mypy src
	PYTHONPATH=src lint-imports
	@echo "✅ Linting complete!"

format: ## コードのフォーマットをチェック（ruff format --check）
	@echo "🔍 Checking code format..."
	uv run ruff format src
	uv run ruff check --fix src
	@echo "✅ Format complete!"
