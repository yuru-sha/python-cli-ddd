import argparse

from ...application.usecases.message.print_message_usecase import (
    PrintMessageInput,
    PrintMessageUseCase,
)
from ...infrastructure.config.settings import settings
from ...infrastructure.logging.logger import logger


def main() -> None:
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="メッセージを出力するバッチ処理")
    parser.add_argument("message", help="出力するメッセージ")
    args = parser.parse_args()

    # 環境設定の表示（デバッグモードの場合）
    if settings.DEBUG:
        logger.debug(f"Running in {settings.APP_ENV} mode")

    # ユースケースの実行
    logger.info("Starting message processing")
    try:
        usecase = PrintMessageUseCase()
        result = usecase.execute(PrintMessageInput(message=args.message))

        # 結果の出力
        print(f"Message: {result.formatted_message}")
        print(f"Timestamp: {result.timestamp}")
        logger.info("Message processing completed successfully")
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise


if __name__ == "__main__":
    main()
