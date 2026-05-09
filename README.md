# 🌍 AI Trip Planner

You tell it where you want to go. It figures out the rest — weather, places, currency, itinerary — by calling the right APIs through a LangGraph ReAct agent running on Groq.

🔗 **Live Demo:** https://kopalverma24-ai-trip-planner.hf.space

---

## What it actually does

- Builds multi-day trip itineraries with hotels and activities
- Checks live weather at your destination
- Converts currency (useful when you're budgeting in INR but booking in EUR)
- Finds places via Google Places and Foursquare
- Pulls recent travel info using Tavily web search

It's not a chatbot that gives generic travel advice. The agent decides which tools to call based on your query and chains them together.

## Tech Stack

| Layer    | Tools                                                                   |
|-------   |-------                                                                  |
| Agent    | LangGraph ReAct + Groq (LLaMA 3)                                        |
| Backend  | FastAPI                                                                 |
| Frontend | Streamlit                                                               |
| APIs     | Google Places, Foursquare, Tavily, OpenWeatherMap, ExchangeRate, OpenAI |

## Run locally

```bash
git clone https://github.com/kopalverma24/AI_Trip_Planner.git
cd AI_Trip_Planner
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=
OPENAI_API_KEY=
GOOGLE_API_KEY=
GPLACES_API_KEY=
FOURSQUARE_API_KEY=
TAVILY_API_KEY=
OPENWEATHERMAP_API_KEY=
EXCHANGE_RATE_API_KEY=
LANGCHAIN_API_KEY=
```

Then run both servers:
```bash
# Terminal 1
uvicorn main:app --reload

# Terminal 2
streamlit run streamlit_app.py
```

## Project Structure

```
AI_Trip_Planner/
├── agent/
│   └── agentic_workflow.py   # LangGraph ReAct agent
├── tools/                    # Tool integrations (weather, places, currency etc.)
├── utils/                    # Helpers
├── main.py                   # FastAPI backend
├── streamlit_app.py          # Streamlit frontend
└── requirements.txt
```

---

Built by **Kopal Verma** — B.Tech CSE, VIT Bhopal  
[GitHub](https://github.com/kopalverma24) | [LinkedIn](https://linkedin.com/in/kopalverma)
