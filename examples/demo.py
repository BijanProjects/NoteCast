"""Demonstration of using the NoteCast components."""
import os
import sys

# Allow running the example without installing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from notecast.transcription import Segment
from notecast.store import DocumentStore
from notecast.chatbot import ChatBot


def main():
    # Placeholder conversation data
    segments = [
        Segment(start=0.0, end=1.0, speaker="Alice", text="Hi everyone"),
        Segment(start=1.0, end=2.0, speaker="Bob", text="Let's discuss the report"),
        Segment(start=2.0, end=3.0, speaker="Alice", text="Sure, go ahead"),
    ]

    store = DocumentStore()
    store.add_segments(segments)

    bot = ChatBot(store)
    answer = bot.ask("report")
    print(answer)


if __name__ == "__main__":
    main()
