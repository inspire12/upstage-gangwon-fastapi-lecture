from typing import AsyncGenerator
from app.models.schemas.chat import ChatRequest
from app.repository.client.upstage_client import UpstageClient


class ChatService:
    def __init__(self, upstage_client: UpstageClient):
        self.client = upstage_client
    
    async def chat(self, message: ChatRequest) -> AsyncGenerator[str, None]:
        """기본 채팅"""
        async for chunk in self.client.chat_streaming(message):
            yield chunk

    # 이전 버전 호환성
    async def upstage_chat(self, message: ChatRequest):
        async for chunk in self.client.chat_streaming(message):
            yield chunk

    def upstage_chat_function_calling(self, prompt: str = "서울 날씨 어때?"):
        """간단한 함수 호출 예제"""
        return self.client.chat_with_tools(prompt)