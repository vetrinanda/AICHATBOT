# AI Chatbot Assistant

A modern, intelligent chatbot application built with **FastAPI**, **LangChain**, and **Google Generative AI**. This project features a robust Python backend and a sleek, responsive frontend interface.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688.svg)

## 🌟 Features

- **Intelligent Conversations**: Powered by Google's Gemini models via LangChain.
- **Context Awareness**: Maintains chat history for more natural interactions (session-based).
- **Modern UI**:
  - Dark mode aesthetic with glassmorphism effects.
  - Responsive design for mobile and desktop.
  - Real-time typing indicators.
  - Markdown rendering for rich text responses.
- **Robust Backend**: Built on FastAPI for high performance and easy API extension.

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Uvicorn
- **AI/LLM**: LangChain, Google Generative AI (Gemini)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (No heavy frameworks)
- **Package Manager**: `uv` (recommended) or `pip`

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.10 or higher
- A Google Cloud API Key for Gemini (Generative AI)
- [uv](https://github.com/astral-sh/uv) (optional, but recommended for fast dependency management)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>
   ```

2. **Set up the environment**
   
   Create a `.env` file in the root directory based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
   
   Open `.env` and add your API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   MODEL_NAME=gemini-pro
   TEMPERATURE=0.7
   ```

3. **Install Dependencies**

   Using `uv` (Recommended):
   ```bash
   uv sync
   # OR if you just want to install from requirements
   uv pip install -r requirements.txt
   ```

   Using standard `pip`:
   ```bash
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running the Application

1. **Start the Backend Server**
   ```bash
   # Using uv
   uv run main.py
   
   # OR using python directly
   python main.py
   ```
   The server will start at `http://localhost:8000`.

2. **Launch the Frontend**
   - Navigate to the `Frontend` folder.
   - Open `index.html` in your web browser.
   - Start chatting!

## 📁 Project Structure

```
├── agents/
│   └── agent.py          # LangChain agent logic and memory management
├── Frontend/
│   ├── index.html        # Main chat interface
│   ├── style.css         # Styling and animations
│   └── script.js         # Frontend logic and API integration
├── main.py               # FastAPI application entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (Ignored by Git)
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
