# Academic Notification Engine

A personal project I'm building to learn AI systems, LangChain, and backend development.

The idea is simple — university notice boards are chaotic. This system reads academic notices, figures out what's important, and tells you about it intelligently.

Still in progress.

---

## What it does (so far)

- Accepts raw notice text via a REST API
- Uses an LLM to extract the title, summary, deadlines, category, and priority
- Saves parsed notices to MongoDB
- Returns structured JSON you can actually use

---

## Stack

- **FastAPI** — API server
- **Groq (LLaMA 3.3 70B)** — LLM for parsing and classification
- **MongoDB Atlas** — storing notices
- **Chroma** — vector search (coming soon)
- **LangChain** — agent orchestration (coming soon)

---

## Running it locally

```bash
# Clone and set up
git clone https://github.com/saumya/academic-notifier.git
cd academic-notifier

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Add your keys to .env
cp .env.example .env

# Start the server
uvicorn backend.main:app --reload
```

Then open `http://localhost:8000/docs` to try it out.

---

## Environment variables

```
GROQ_API_KEY=
ANTHROPIC_API_KEY=
MONGODB_URI=
MONGODB_DB_NAME=academic_notifier
APP_ENV=development
```

---

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check server is running |
| POST | `/notices/parse` | Parse a notice with AI |
| GET | `/notices/all` | Get all stored notices |
| GET | `/notices/priority/{level}` | Filter by high / medium / low |

---

## What I'm building next

- Semantic search with Chroma so you can query notices by meaning
- User profiles so the system knows what's relevant to you
- Deadline reminders and action triggers
- React frontend
- AWS deployment

---

## Why I built this

I'm a CS undergrad learning how AI systems actually get built end to end — not just calling an API, but proper architecture with agents, memory, databases, and deployment. This is that project.

---

*Saumya*