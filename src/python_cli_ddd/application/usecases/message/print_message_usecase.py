from dataclasses import dataclass

from ....domain.models.message import Message


@dataclass
class PrintMessageInput:
    message: str


@dataclass
class PrintMessageOutput:
    formatted_message: str
    timestamp: str


class PrintMessageUseCase:
    def execute(self, input_data: PrintMessageInput) -> PrintMessageOutput:
        # ドメインオブジェクトの作成
        message = Message.create(content=input_data.message)

        # 出力の作成
        return PrintMessageOutput(
            formatted_message=message.content, timestamp=message.created_at.isoformat()
        )
