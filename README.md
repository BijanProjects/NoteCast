# NoteCast

NoteCast is a prototype project for generating notes and reports from meeting
recordings. The repository contains a minimal retrieval-augmented chatbot that
works with transcribed audio segments. The system is designed to support
speaker-aware transcripts and provide simple question answering over those
transcripts.

## Features

- **Speaker segmentation** and transcription placeholders.
- **In-memory document store** for storing conversation segments.
- **Retrieval-augmented chatbot** that searches the store and generates simple
  answers based on the retrieved context.

## Example

Run the demonstration script:

```bash
python examples/demo.py
```

This uses placeholder data to show how the chatbot API works. Integrating real
speech recognition, speaker diarization, and language models is left as future
work.
