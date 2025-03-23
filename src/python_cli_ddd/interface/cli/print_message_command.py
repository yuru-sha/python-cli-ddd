import argparse

from typing import TYPE_CHECKING

from python_cli_ddd.application.usecases.message.print_message_usecase import PrintMessageInput
from python_cli_ddd.infrastructure.di.container import ApplicationContainer
from python_cli_ddd.infrastructure.logging.logger import logger

if TYPE_CHECKING:
    from python_cli_ddd.core.di.interfaces import DIContainer


def main() -> None:
    # DIコンテナの初期化
    container: DIContainer = ApplicationContainer()
    container.init_resources()

    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="メッセージを出力するバッチ処理")
    parser.add_argument("message", help="出力するメッセージ")
    args = parser.parse_args()

    # デバッグモードの場合は環境設定を表示
    if container.config.get_bool("DEBUG"):
        logger.debug(f"Running in {container.config.get_str('APP_ENV')} mode")

    # ユースケースの実行
    logger.info("Starting message processing")
    try:
        usecase = container.print_message_usecase()
        result = usecase.execute(PrintMessageInput(message=args.message))

        # 結果の出力
        print(f"Message: {result.formatted_message}")
        print(f"Timestamp: {result.timestamp}")
        logger.info("Message processing completed successfully")
    except Exception as e:
        logger.error(f"Error processing message: {e!s}")
        raise


if __name__ == "__main__":
    main()
