# AI Product Intelligence Suite

AI-powered platform for **product intelligence, market intelligence, competitor analysis, trends, and strategic insights** using Generative AI.

## 👨‍💻 Developer

**Kalyana Sundar**  
AI / ML Engineer | Generative AI | Python | Data Science

---

## 🚀 Live Demo

**Application:**  
https://ai-pro-intelligence-suite-kalyanasundar.streamlit.app/

**GitHub:**  
https://github.com/sundar66kalyan/AI_Product_Intelligence_Suite

---

## ✨ Features

- 📊 Market Intelligence Dashboard
- 🔎 Product Intelligence
- 🏆 Competitor Analysis
- 📈 Market Trends
- 📰 News & Technology Signals
- 🤖 Gemini AI Market Analysis
- 🧠 AI Insights
- 🎨 AI Moodboard
- 📄 AI-generated Reports
- 🕘 Analysis History
- 🔌 REST APIs

---

## 🏗️ Architecture

```text
                 User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
            FastAPI Backend
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
    Market     Product      AI
   Services   Services   Services
       │          │          │
       └──────────┼──────────┘
                  ▼
             Google Gemini
                  │
                  ▼
          AI Insights / Reports
                  │
                  ▼
          SQLAlchemy + SQLite

🛠️ Technology Stack
Frontend
Python
Streamlit
Plotly
Requests
Backend
FastAPI
Uvicorn
Pydantic
Pydantic Settings
AI
Google Gemini
Generative AI
Prompt Engineering
Structured AI Responses
Database
SQLite
SQLAlchemy
Data & Intelligence
Pandas
Google Trends
News Sources
Hacker News
Deployment
Docker
Docker Networking
Streamlit Cloud
Git / GitHub
📁 Project Structure

AI_Product_Intelligence_Suite/
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── api/
│       ├── core/
│       ├── database/
│       ├── models/
│       ├── modules/
│       ├── services/
│       └── utils/
│
├── frontend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   ├── components/
│   ├── services/
│   │   └── api.py
│   └── pages/
│       ├── 1_Market_Dashboard.py
│       ├── 2_AI_Insights.py
│       ├── 3_Product_Search.py
│       ├── 4_History.py
│       └── 5_Gemini_Report.py
│
├── .gitignore
└── README.md

▶️ Run Locally
1. Clone
git clone https://github.com/sundar66kalyan/AI_Product_Intelligence_Suite.git
cd AI_Product_Intelligence_Suite
2. Create Virtual Environment
python -m venv .venv
.venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r backend\requirements.txt
pip install -r frontend\requirements.txt
4. Configure .env

Create a .env file in the project root:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
DATABASE_URL=sqlite:///./data/market_intelligence.db
API_BASE_URL=http://127.0.0.1:8000

Never commit your real API key to GitHub.

▶️ Start Backend

Open Terminal 1:

cd D:\AI_Product_Intelligence_Suite
.venv\Scripts\Activate.ps1
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

Backend:

http://127.0.0.1:8000

Health check:

http://127.0.0.1:8000/health

API documentation:

http://127.0.0.1:8000/docs
▶️ Start Frontend

Open Terminal 2:

cd D:\AI_Product_Intelligence_Suite
.venv\Scripts\Activate.ps1
streamlit run frontend\app.py

Open:

http://localhost:8501
Local Architecture
Streamlit :8501
     │
     ▼
FastAPI :8000
     │
     ├── SQLite
     ├── Gemini
     └── Market APIs
🐳 Run with Docker

Build images:

docker build -t ai-product-backend:latest backend
docker build -t ai-product-frontend:latest frontend

Create network:

docker network create ai-product-network

Start backend:

docker run -d --name ai-backend `
  --network ai-product-network `
  -p 8000:8000 `
  ai-product-backend:latest

Start frontend:

docker run -d --name ai-frontend `
  --network ai-product-network `
  -p 9000:8501 `
  ai-product-frontend:latest

Open:

http://localhost:9000

In Docker, the frontend communicates with the backend using http://ai-backend:8000.

🔌 Main API Endpoints
Endpoint	Method	Purpose
/health	GET	Health check
/market/snapshot	GET	Market snapshot
/market/google-trends	GET	Market trends
/market/news	GET	News
/market/hacker-news	GET	Technology signals
/market-dashboard/	GET	Dashboard data
/ai/market-analysis	GET	AI market analysis
/ai-insights/	GET	AI insights
/product-intelligence/analyze	GET	Product analysis
/history/	GET	Analysis history
/history/{id}	GET	History item
/moodboard/	POST	Moodboard generation
/gemini-report/	POST	AI report generation
🔄 AI Workflow
Product / Market Input
        ↓
Market & Product Data
        ↓
Trend / News Signals
        ↓
Context Preparation
        ↓
Google Gemini
        ↓
AI Analysis
        ↓
Structured Output
        ↓
History / Reports
        ↓
Streamlit Dashboard
🔐 Security
API keys are stored in environment variables.
.env should not be committed.
Backend and frontend are separated.
AI credentials are not exposed directly to the frontend.
Production deployment should use HTTPS and proper secret management.
📈 Future Improvements
PostgreSQL
Redis caching
Authentication
Role-based access
CI/CD
Automated testing
LLM evaluation
Monitoring
Background AI workers
Production-scale deployment
💼 Resume Value

This project demonstrates practical experience in:

Generative AI • LLM Integration • FastAPI • Streamlit • REST APIs • SQLAlchemy • SQLite • Docker • Docker Networking • Cloud Deployment • GitHub

👨‍💻 Developer

Kalyana Sundar

AI / ML Engineer | Generative AI | Python | Data Science

Built as an end-to-end AI Engineering portfolio project.