# Jarvis: Pre-AI Voice Assistant

> A fully functional voice assistant built in 8th grade (2020), demonstrating foundational concepts in speech processing, API integration, and system automation before the LLM era.

This repository contains the original Jarvis codebase—a keyword-matching voice assistant that showcases how conversational interfaces worked before large language models. It's a genuine learning artifact: real engineering, authentic limitations, and honest code.

## Capabilities

Jarvis can:
- **Listen & respond** — Speech-to-text recognition and text-to-speech output
- **Answer questions** — Wikipedia search integration
- **Fetch data** — Real-time weather via web scraping
- **Communicate** — Send emails through Gmail
- **Browse content** — Fetch NASA's Astronomy Picture of the Day
- **Capture media** — Screenshot functionality
- **Control playback** — Media control commands
- **Retrieve info** — Dictionary definitions and random jokes
- **Launch apps** — Execute keyboard shortcuts and open applications

## How It Works

Jarvis is a **keyword-matching command router**:

```
Listen → Transcribe → Match Keywords → Execute → Respond
```

Commands are hardcoded as if/elif branches:
- `if 'wikipedia' in query:` → search Wikipedia
- `if 'weather' in query:` → scrape weather
- `if 'email' in query:` → send email

**Trade-off:** Simple and effective for ~50 commands, but requires exact keywords and doesn't generalize to phrasing variations.

## Limitations

This is pre-LLM technology, with expected trade-offs:

- **No intent parsing** — Requires exact keywords; can't handle phrasing variations
- **Stateless** — No conversation memory or context awareness
- **Limited scale** — Effective for ~50 commands; doesn't generalize beyond that
- **Fragile integrations** — Web scraping breaks when pages change; basic error handling
- **Platform-specific** — Windows file paths; limited cross-platform support

## Quick Start

**Requirements:**
- Python 3.7+
- Microphone & speakers
- Internet connection
- Gmail account (for email feature)
- NASA API key (free at https://api.nasa.gov)

**Setup:**

1. Clone and navigate to the repository
   ```bash
   git clone https://github.com/Simp0099/jarvis.git
   cd jarvis
   ```

2. Create virtual environment and install dependencies
   ```bash
   python -m venv venv

   Mac Os :
   source venv/bin/activate   
   Windows: 
   venv\Scripts\activate

   pip install -r requirements.txt
   ```

3. Configure environment variables
   ```bash
   cp .env.example .env
   # Edit .env with your credentials:
   # GMAIL_USER=your_email@gmail.com
   # GMAIL_PASSWORD=your_app_password (use app-specific password)
   # NASA_API_KEY=your_key
   ```

4. Run
   ```bash
   python Jarvis.py
   ```

## Example Commands

Once running, try:

```
"What's the weather?"              → Reads current weather
"Who is Elon Musk?"                → Searches Wikipedia
"Email John"                        → Sends email
"Take a screenshot"                 → Captures screen
"Tell me a joke"                    → Random joke
"Show today's space picture"        → NASA APOD
"Open Chrome"                       → Launches applications
```

## Project Structure

```
jarvis/
├── Jarvis.py            # Main assistant
├── Nasa.py              # NASA API module
├── requirements.txt     # Dependencies
├── .env.example         # Config template
├── README.md            # This file
└── Resources/           # Audio, images, data
```

## Context

Built in 2020 (pre-LLM era, before ChatGPT launched in Nov 2022), this project demonstrates:

- **Pre-LLM Architecture** — How voice assistants operated with keyword matching instead of neural language understanding
- **Real Engineering** — Multi-library integration, API handling, speech processing, and system automation
- **Honest Learning** — Includes authentic limitations and design trade-offs; more educational than sanitized code
- **Early Initiative** — Independent 8th-grade project showing systems thinking and follow-through

## Modernization Roadmap

A complete 6-phase upgrade path exists to transform Jarvis into an LLM-powered agent:

1. **Foundation fixes** — Remove hardcoded paths, move to .env
2. **LLM integration** — Replace keyword matching with Claude/GPT-4 function calling
3. **Memory** — Add conversation history and context awareness
4. **Better I/O** — Upgrade STT/TTS and add wake-word detection
5. **Real-world actions** — Safe tool execution with proper error handling
6. **Production** — Logging, service management, configuration

See the full roadmap in `MODERNIZATION_GUIDE.pdf` (included).

## Evolution to LLM

Want to see the modern version? Check **[jarvis-ai](https://github.com/Simp0099/jarvis-ai)** — the LLM-powered successor.

**The Story in Two Repos:**

| | v1 (This Repo) | v2 (jarvis-ai) |
|---|---|---|
| **Year** | 2020 | 2024 |
| **Core** | Keyword matching | LLM + function calling |
| **Scale** | ~50 commands | Natural language |
| **Memory** | None | Full conversation history |
| **Intent** | String patterns | LLM understanding |

**To modernize your instance:** Follow the 6-phase roadmap in `MODERNIZATION_GUIDE.pdf`.

## License

MIT License — Learn, modify, and build on this freely.

---

**A learning project from 2020:** This repo preserves the original pre-LLM architecture. The modernized version lives in [jarvis-ai](https://github.com/Simp0099/jarvis-ai). Together they tell a story about building systems, learning from constraints, and evolving with technology.
