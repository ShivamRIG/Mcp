# Email Task Assistant — MCP Server

An MCP (Model Context Protocol) server that reads your emails, extracts actionable tasks using Groq LLM via LangChain, and keeps track of them so you never miss a deadline.

---

## Features

- Fetch unread emails via IMAP
- Extract tasks and summaries from emails using Groq LLM (LLaMA 3.3 70B) via LangChain
- Save, list, and mark tasks as done
- Plugs directly into Claude Desktop as an MCP tool
- Telegram reminders (coming soon)

---

## Project Structure

```
Mcp/
├── app/
│   ├── llm.py          # LangChain + Groq task extraction chain
│   ├── mail.py         # IMAP email fetching and body extraction
│   └── Server.py       # MCP server — exposes tools to Claude
├── config/
│   └── config.py       # Environment variable loader
├── test/
│   ├── test_llm.py     # LLM and full flow tests
│   └── test.py         # Unit tests
├── .env                # Secrets (never commit this)
├── .gitignore
├── mail.json           # Email processing state
├── tasks.json          # Local task store (auto-created)
└── README.md
```

---

## MCP Tools

| Tool | Description |
|---|---|
| `get_unread_email` | Fetches unread emails from your inbox |
| `summarize_email` | Extracts tasks and summary from an email using Groq |
| `add_task` | Manually add a task to the list |
| `list_pending_tasks` | Returns all tasks not yet marked done |
| `mark_email_processed` | Marks a task as done by ID |

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/email-mcp-assistant.git
cd email-mcp-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv testenv
source testenv/bin/activate       # Mac/Linux
testenv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install langchain langchain-groq langchain-core python-dotenv mcp
```

### 4. Create your `.env` file

```env
# Email
Email_Address=you@example.com
Email_Password=your_email_password
IMAP_Server=mail.uni.kl.de
IMAP_port=993
GMAIL=imap.gmail.com

# Groq
GROQ_API_KEY=gsk_your_groq_key_here

# Telegram (optional)
Telegram_bot_token=your_telegram_bot_token
Session=your_telegram_chat_id
```

Never commit `.env` to Git — it is already in `.gitignore`.

### 5. Get your free Groq API key

Sign up at [console.groq.com](https://console.groq.com) — free and very fast.

---

## Running the Server

```bash
python app/Server.py
```

The server communicates via JSON-RPC and is meant to be connected to an MCP client like Claude Desktop. Do not type into it directly.

---

## Testing

Run the full end-to-end test:

```bash
python test/test_llm.py
```

This will fetch your real unread emails, extract tasks using Groq, save them to `tasks.json`, and print all pending tasks.

Test individual components:

```bash
# Test LLM only
python -c "from app.llm import extract_tasks_from_email; print(extract_tasks_from_email('Meeting', 'Submit report by Friday'))"

# Test email fetching only
python -c "from app.mail import get_unread_emails; print(get_unread_emails())"

# Test task listing only
python -c "from app.Server import list_pending_tasks; print(list_pending_tasks())"
```

---

## Connect to Claude Desktop

Add this to your Claude Desktop config file:

- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "email-assistant": {
      "command": "python",
      "args": ["/absolute/path/to/Mcp/app/Server.py"]
    }
  }
}
```

Restart Claude Desktop and your email tools will appear automatically.

---

## Tech Stack

| Layer | Technology |
|---|---|
| MCP Framework | FastMCP |
| LLM Provider | Groq (LLaMA 3.3 70B) |
| LLM Orchestration | LangChain |
| Email Protocol | IMAP via Python imaplib |
| Task Storage | JSON file (SQLite planned) |
| Notifications | Telegram Bot (coming soon) |

---

## Roadmap

- [x] Fetch unread emails via IMAP
- [x] Extract tasks using Groq LLM
- [x] Save and manage tasks locally
- [ ] Telegram daily reminder digest
- [ ] SQLite persistent database
- [ ] Email deduplication (avoid re-processing the same email)
- [ ] Web dashboard for task management

---

## Contributing

Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.

---
