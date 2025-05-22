"""Retrieval-augmented chatbot for meeting notes."""
from dataclasses import dataclass
from typing import List

from .store import DocumentStore
from .transcription import Segment

@dataclass
class ChatBot:
    store: DocumentStore

    def ask(self, question: str) -> str:
        """Return an answer to the user's question based on stored segments."""
        relevant_segments: List[Segment] = self.store.search(question)
        context = "\n".join(f"{s.speaker}: {s.text}" for s in relevant_segments)
        if not context:
            return "I'm sorry, I couldn't find anything related to your question."
        # TODO: integrate with a language model to generate a more detailed answer.
        # For now we simply echo the retrieved context.
        return f"Here is what I found:\n{context}"
