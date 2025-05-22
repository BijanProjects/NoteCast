"""Top-level package for NoteCast."""

from .transcription import Segment, transcribe_audio
from .store import DocumentStore
from .chatbot import ChatBot

__all__ = [
    "Segment",
    "transcribe_audio",
    "DocumentStore",
    "ChatBot",
]
