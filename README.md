# chatbot

A configurable console-based chatbot demonstrating how a stateless LLM API
can be used to simulate stateful conversational behavior.

---

## Features

- Interactive command-line chat interface
- Consistent assistant personality via system prompt
- Correct handling of system, user, assistant, and tool roles
- In-memory conversation state
- Tool calling support
- Conversation summarization on demand
- Fully configurable via CLI arguments

---

## Architecture Overview

The OpenAI API is stateless by design.  
This application simulates state by maintaining an in-memory message history
that is sent with each request.


