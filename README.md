# AI Chatbot Assistant

A lightweight chatbot application using FastAPI, LangChain, and Google Generative AI. The repo contains a Python backend and a minimal frontend under `Frontend/` for local testing.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)

## Features

- Intelligent conversations via LangChain + Google Generative AI (Gemini-compatible)
- Session-aware chat history (simple in-memory/session handling)
- Minimal responsive frontend with Markdown rendering

## Tech Stack

- **Backend**: Python, FastAPI (served directly or with Uvicorn)
- **AI/LLM**: LangChain + Google Generative AI
- **Frontend**: HTML, CSS, Vanilla JavaScript

## Getting Started

These instructions assume you're working from the repository root: `d:\Projects\AICHATBOT`.

### Prerequisites

- Python 3.10 or newer
- A Google Cloud API Key for Generative AI (Gemini)

### Setup

1. Create environment file

   - Cross-platform (PowerShell / Unix):

     ```powershell
     copy .env.example .env
     ```

   - Edit `.env` and add your credentials:

     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     MODEL_NAME=gemini-pro
     TEMPERATURE=0.7
     ```

2. Install Python dependencies

   ```powershell
   pip install -r requirements.txt
   ```

   (If you use `uv`, you can also run `uv sync` or `uv pip install -r requirements.txt`.)

### Running the app

1. Start the backend API (development)

   ```powershell
   python main.py
   ```

   Or run with `uv` if configured:

   ```powershell
   uv run main.py
   ```

   By default the API listens on `http://localhost:8000` unless configured otherwise.

2. Open the frontend

   - Open `Frontend\index.html` in your browser to interact with the UI.

## Project Structure

```
.
├── agents/
│   ├── __init__.py      # agents package
│   └── chat.py          # chat/agent logic used by the backend
├── Frontend/
│   ├── index.html       # minimal chat UI
│   ├── script.js        # frontend API integration + UI logic
│   └── style.css        # styling
├── main.py              # FastAPI application entry point
├── pyproject.toml       # project metadata (optional)
├── requirements.txt     # Python dependencies
├── README.md            # this file
└── .env                # environment variables (ignored by VCS)
```

## Notes

- The backend entry point is `main.py` and bot/agent logic is in `agents/chat.py`.
- Keep API keys out of source control—use `.env` and add it to `.gitignore`.

## Contributing

Contributions welcome. Create a branch, make changes, and open a pull request.

## License

This project is provided under the MIT license.
