# chatbot

A configurable console-based chatbot for user-assistant conversation.

---

## Features

- Interactive command-line chat interface
- Consistent assistant personality via system prompt
- In-memory conversation state
- Tool calling support
- Conversation summarization on demand
- Fully configurable via CLI arguments

---

## Architecture Overview

The OpenAI API is stateless by design.  
This application simulates state by maintaining an in-memory message history
that is sent with each request.

---

## Requirements

See requirements.txt

Install dependencies:

pip install -r requirements.txt

## Environment Configuration

This project uses `python-dotenv` for local development.

1. Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your-api-key

## Usage

Run the chatbot:

Run:
```bash
python main.py
```
