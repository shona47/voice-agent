# 🎙️ Voice AI Personal Assistant

An intelligent, voice-controlled personal assistant built using Python, Whisper, Ollama, and various automation tools. It understands natural language commands, plans tasks, and executes actions such as sending emails, searching the web, managing reminders, and remembering previous interactions.

## 🚀 Features

- **Voice Input:** Captures user commands through a microphone.
- **Speech Recognition:** Converts speech into text using OpenAI Whisper.
- **LLM-Based Planning:** Uses Qwen 2.5 (1.5B) through Ollama to understand user intent and determine the appropriate action.
- **Email Automation:** Integrates with Gmail to compose and send emails.
- **Web Search:** Retrieves relevant information using Tavily.
- **Reminder Management:** Creates reminders, checks pending tasks, and sends notifications.
- **Long-Term Memory:** Uses ChromaDB to store and retrieve relevant user information.
- **Conversation History:** Maintains interaction history using SQLite.
- **Text-to-Speech:** Uses Piper TTS to generate voice responses.
- **Action Confirmation:** Requests confirmation before executing sensitive actions.

## 🏗️ System Architecture

```text
          User Voice Input
                 |
                 v
          Audio Recorder
                 |
                 v
           Whisper STT
                 |
                 v
          Qwen LLM (Ollama)
                 |
                 v
           Task Planner
                 |
                 v
          Tool Registry
                 |
       +---------+---------+
       |         |         |
       v         v         v
     Gmail    Web Search  Reminder
       |         |         |
       +---------+---------+
                 |
                 v
          Memory & History
                 |
                 v
             Piper TTS
                 |
                 v
          Voice Response
```

## 🛠️ Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| Speech-to-Text | OpenAI Whisper |
| Large Language Model | Qwen 2.5 (1.5B) |
| LLM Runtime | Ollama |
| Text-to-Speech | Piper |
| Vector Database | ChromaDB |
| Database | SQLite |
| Web Search | Tavily API |
| Email Integration | Gmail API |

## 📂 Project Structure

```text
voice-agent/
│
├── app/
│   ├── agent/
│   │   ├── planner.py
│   │   ├── executor.py
│   │   ├── confirmation.py
│   │   └── tool_registry.py
│   │
│   ├── config/
│   │   └── config.py
│   │
│   ├── llm/
│   │   └── qwen.py
│   │
│   ├── memory/
│   │   └── memory.py
│   │
│   ├── speech/
│   │   ├── recorder.py
│   │   ├── whisper_stt.py
│   │   └── tts.py
│   │
│   └── tools/
│       ├── email.py
│       ├── search.py
│       ├── reminder.py
│       ├── reminder_checker.py
│       ├── history.py
│       ├── memory_rag.py
│       └── chat.py
│
├── main.py
├── run_reminder_checker.py
├── test_memory.py
├── test_planner.py
├── test_reminder.py
├── test_search.py
├── test_tts.py
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shona47/voice-agent.git
cd voice-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Ollama

Install Ollama from [https://ollama.com/](https://ollama.com/).

Download the required model:

```bash
ollama pull qwen2.5:1.5b
```

Make sure Ollama is running before starting the assistant.

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
```

Add any other configuration variables required by your application.

### 6. Configure Gmail API

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Create or select a Google Cloud project.
3. Enable the Gmail API.
4. Configure OAuth consent and create OAuth client credentials.
5. Download the OAuth credentials as `credentials.json`.
6. Place the file in the project root.

The application may generate `token.json` during authentication.

**Never upload API keys, OAuth credentials, or access tokens to GitHub.**

### 7. Configure Piper TTS

Download the Piper voice model and its corresponding JSON configuration.

Place both files inside:

```text
app/speech/models/
```

The expected model files are:

```text
en_US-lessac-medium.onnx
en_US-lessac-medium.onnx.json
```

### 8. Run the Assistant

```bash
python main.py
```

Speak into your microphone and interact with your personal AI assistant.

### 9. Run the Reminder Checker

To check and process pending reminders separately:

```bash
python run_reminder_checker.py
```

## 🔐 Security

- API keys and credentials are stored locally.
- Sensitive files are excluded using `.gitignore`.
- Confirmation is required before sensitive actions.
- Gmail authentication uses OAuth.

## 🔮 Future Enhancements

- Improved contextual understanding and multi-turn conversations.
- More integrations with external applications.
- Enhanced personalized memory retrieval.
- Improved voice interaction and response speed.
- Additional intelligent task automation.

## 👩‍💻 Author

**Shona Balaji**

B.Tech – Artificial Intelligence and Data Science

GitHub: [@shona47](https://github.com/shona47)

---

⭐ If you find this project interesting, consider giving the repository a star!
