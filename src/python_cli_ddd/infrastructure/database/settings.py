"""データベース設定

このモジュールは、データベース接続の設定を管理します。
"""

from pathlib import Path

from python_cli_ddd.infrastructure.config.settings import settings

# データベースファイルのパス
DB_FILE = Path(settings.get_str("DB_FILE", str(Path.cwd() / "tasks.db")))
DB_FILE.parent.mkdir(parents=True, exist_ok=True)

# データベースURL
DATABASE_URL = f"sqlite:///{DB_FILE}"
