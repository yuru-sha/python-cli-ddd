from dataclasses import dataclass

from python_cli_ddd.domain.models.message import Message


@dataclass
class PrintMessageInput:
    """メッセージ出力ユースケースの入力値オブジェクト"""

    message: str


@dataclass
class PrintMessageOutput:
    """メッセージ出力ユースケースの出力値オブジェクト"""

    formatted_message: str
    timestamp: str


class PrintMessageUseCase:
    """メッセージを出力するユースケース"""

    def execute(self, input_data: PrintMessageInput) -> PrintMessageOutput:
        """ユースケースを実行する"""
        message = Message.create(content=input_data.message)
        return PrintMessageOutput(
            formatted_message=message.format_message(),
            timestamp=message.timestamp.isoformat(),
        )
