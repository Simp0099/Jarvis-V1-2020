# Quick Setup Guide

## 1. Clone & Install (5 minutes)

```bash
git clone https://github.com/YOUR_USERNAME/jarvis.git
cd jarvis
pip install -r requirements.txt
```

## 2. Get API Keys

**NASA API (Free)**
- Go to https://api.nasa.gov
- Sign up with your email
- Copy your API key

**Gmail (Free)**
- Enable 2-Factor Authentication on your Google account
- Go to https://myaccount.google.com/apppasswords
- Generate an app password for "Mail" on "Windows Computer"
- Copy the 16-character password

## 3. Configure

```bash
cp .env.example .env
```

Edit `.env` with your actual values:
```
GMAIL_USER=your_actual_email@gmail.com
GMAIL_PASSWORD=your_16_char_app_password
NASA_API_KEY=your_actual_api_key
```

**Important:** Never commit `.env` — it's in .gitignore and protected.

## 4. Run

```bash
python Jarvis.py
```

When you see `"Listening..."` the assistant is active.

## What Works

✓ Weather checking  
✓ Wikipedia searches  
✓ NASA astronomy pictures  
✓ Email sending  
✓ Screenshots  
✓ Jokes  
✓ Dictionary lookups  
✓ Media control  
✓ Application launching  

## Known Limitations

✗ Exact keyword matching required  
✗ No memory between sessions  
✗ Windows-only file paths (hardcoded)  
✗ Requires stable internet  
✗ Google weather scraping is fragile  

## Troubleshooting

**"Microphone not found"**
- Check your system has a working microphone
- Run a test: `python -c "import speech_recognition; print(speech_recognition.Microphone().list_microphone_indexes())"`

**"Gmail login failed"**
- Make sure you're using the app-specific password, not your Gmail password
- Check 2FA is enabled: https://myaccount.google.com/security

**"NASA API error"**
- Check your API key is correct
- Verify internet connection
- NASA API has rate limits (50/hour free tier)

**"Weather not working"**
- Google changes their HTML frequently — the CSS selector may be outdated
- Consider upgrading to OpenWeatherMap API (Phase 1 improvement)

## Next: Modernize

Once this is working, see [MODERNIZATION_GUIDE.pdf](Modernization_Guide.pdf) for how to upgrade to an LLM-powered version that:
- Understands natural language
- Remembers conversation history
- Scales to unlimited commands
- Handles phrasing variations

---

Questions? Open an issue on GitHub.
