"""Simple in-memory document store for meeting transcripts."""

from dataclasses import dataclass, field
from typing import List

from .transcription import Segment

@dataclass
class DocumentStore:
    """Stores conversation segments and supports simple retrieval."""
    segments: List[Segment] = field(default_factory=list)

    def add_segments(self, new_segments: List[Segment]) -> None:
        self.segments.extend(new_segments)

    def search(self, query: str, top_k: int = 5) -> List[Segment]:
        """Return segments that contain the query string."""
        query_lower = query.lower()
        results = [s for s in self.segments if query_lower in s.text.lower()]
        return results[:top_k]
