AI Product Intelligence Suite

AI-powered market, product, competitor and strategic intelligence platform

Author: Kalyana Sundar
Project Type: AI Engineering / Generative AI / Market Intelligence
Status: Deployed
Frontend: Streamlit
Backend: FastAPI
AI: Google Gemini
Database: SQLite + SQLAlchemy
Deployment: Streamlit Cloud + Docker
Version Control: Git + GitHub

🚀 Live Demo
🌐 Application

AI Product Intelligence Suite — Live Demo

💻 GitHub Repository

AI Product Intelligence Suite — GitHub

📌 1. Project Overview

The AI Product Intelligence Suite is an end-to-end AI-powered platform designed to analyze products, markets, competitors, trends and strategic opportunities.

The application combines:

Product intelligence
Market intelligence
Competitor analysis
Market trends
News signals
Technology signals
Generative AI
AI-generated reports
Historical analysis
Interactive dashboards
Moodboard generation

The system uses Google Gemini as the generative AI layer and FastAPI as the backend API layer, with Streamlit providing the interactive frontend.

🎯 2. Problem Statement

Businesses need to continuously understand:

What products are gaining demand?
What are competitors doing?
What market trends are emerging?
What opportunities exist?
What risks should businesses consider?
How can product research be performed faster?

Traditional market research often requires manually collecting information from multiple sources.

This project aims to provide a centralized AI-powered platform that brings these signals together and generates structured intelligence.

💡 3. Proposed Solution

The system follows this workflow:

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
Structured Intelligence
        ↓
History / Reports
        ↓
Interactive Dashboard
✨ 4. Key Features
📊 Market Dashboard

Provides an overview of available market intelligence.

Features include:

Market snapshot
Market trends
News signals
Technology signals
AI-generated market analysis
Interactive visualizations
🔎 Product Intelligence

Users can enter a product and generate AI-powered intelligence.

Example:

Product:
ChatGPT

The system can generate:

Executive summary
Strengths
Weaknesses
Opportunities
Threats
Opportunity score
Strategic insights
🤖 AI Market Analysis

The system combines market information with Gemini to generate:

Market insights
Emerging opportunities
Risks
Strategic observations
Product-market signals
🧠 AI Insights

The AI Insights module provides higher-level interpretation of available market information.

The goal is to transform raw information into actionable business intelligence.

🏆 Competitor Intelligence

The platform can be used to analyze competitive positioning and identify:

Competitive strengths
Weaknesses
Market opportunities
Threats
Potential whitespace
🎨 AI Moodboard

The Moodboard module connects product concepts with creative visual directions.

General workflow:

Product / Concept
       ↓
AI Interpretation
       ↓
Creative Direction
       ↓
Moodboard
📄 Gemini Reports

The platform can generate structured AI reports using Gemini.

Reports can include:

Executive Summary
Strengths
Weaknesses
Opportunities
Threats
Strategic Recommendations
🕘 Analysis History

Previous analyses can be stored and retrieved.

Workflow:

AI Analysis
     ↓
History Service
     ↓
SQLAlchemy
     ↓
SQLite

Users can later access previously generated analyses.

🏗️ 5. System Architecture
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │    Streamlit    │
                  │    Frontend     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   API Service   │
                  │    api.py       │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │     FastAPI     │
                  │     Backend     │
                  └────────┬────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Market Services   Product Services   AI Services
          │                │                │
          ▼                ▼                ▼
     Trends / News     Product Data      Gemini
     Tech Signals      Intelligence     LLM
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                     AI Processing
                           │
                           ▼
                   Parser / Validation
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
              SQLAlchemy        API Response
                  │                 │
                  ▼                 ▼
                SQLite          Streamlit
                                    │
                                    ▼
                                   USER
🐳 6. Docker Architecture

The application is separated into two services:

                    Docker
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
   ai-frontend                 ai-backend
   Streamlit                   FastAPI
   Port 8501                   Port 8000
          │                         │
          └──────────┬──────────────┘
                     │
             ai-product-network
Frontend Container
ai-product-frontend
Backend Container
ai-product-backend
Docker Network
ai-product-network

The frontend communicates with the backend using:

http://ai-backend:8000
🛠️ 7. Technology Stack
Programming Language
Python 3.11
Frontend
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
Data
Pandas
Database
SQLite
SQLAlchemy
External Intelligence
Google Trends
News sources
Hacker News
DevOps
Docker
Docker Networking
Git
GitHub
Deployment
Streamlit Cloud
Docker-based local deployment
📁 8. Project Structure
AI_Product_Intelligence_Suite/
│
├── backend/
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   │
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   ├── gemini_report.py
│   │   │   └── history.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── database/
│   │   │   └── init_db.py
│   │   │
│   │   ├── models/
│   │   │   └── history.py
│   │   │
│   │   ├── modules/
│   │   │
│   │   ├── services/
│   │   │   ├── product_service.py
│   │   │   ├── history_service.py
│   │   │   └── llm_service.py
│   │   │
│   │   └── utils/
│   │       └── report_parser.py
│   │
│   └── utils/
│
├── frontend/
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   │
│   ├── components/
│   │
│   ├── services/
│   │   └── api.py
│   │
│   └── pages/
│       ├── 1_Market_Dashboard.py
│       ├── 2_AI_Insights.py
│       ├── 3_Product_Search.py
│       ├── 4_History.py
│       └── 5_Gemini_Report.py
│
├── .gitignore
├── README.md
└── requirements / configuration files
🔄 9. Complete Data Flow

When a user analyzes a product:

1. User enters product
          ↓
2. Streamlit captures input
          ↓
3. frontend/services/api.py
          ↓
4. HTTP request
          ↓
5. FastAPI endpoint
          ↓
6. Product service
          ↓
7. Market/product context
          ↓
8. LLM service
          ↓
9. Gemini
          ↓
10. AI response
          ↓
11. Response parser
          ↓
12. Validation
          ↓
13. History service
          ↓
14. SQLAlchemy
          ↓
15. SQLite
          ↓
16. JSON response
          ↓
17. Streamlit UI
🤖 10. AI Architecture
User Input
    ↓
Context Collection
    ↓
Prompt Construction
    ↓
Gemini
    ↓
Raw AI Response
    ↓
Response Parser
    ↓
Validation
    ↓
Structured Intelligence

The LLM is not directly exposed to the frontend.

Instead:

Streamlit
    ↓
FastAPI
    ↓
LLM Service
    ↓
Gemini

This protects API credentials and keeps AI logic centralized.

🧠 11. Prompt Engineering

Prompts are designed around:

Role
+
Task
+
Context
+
Constraints
+
Output Format

Example conceptual structure:

You are a product-market intelligence analyst.

Analyze the provided product.

Use the supplied market context.

Identify:

- Strengths
- Weaknesses
- Opportunities
- Threats

Return the result in a structured format.

Structured output makes it easier for the backend to process the model response.

💾 12. Database Architecture
FastAPI
   ↓
History Service
   ↓
SQLAlchemy
   ↓
SQLite

SQLite is used because the current application is a lightweight portfolio deployment.

For a larger production system, the recommended evolution is:

SQLite
   ↓
PostgreSQL
🔌 13. Main API Endpoints
Endpoint	Method	Purpose
/health	GET	Health check
/market/snapshot	GET	Market snapshot
/market/google-trends	GET	Google Trends
/market/news	GET	Market news
/market/hacker-news	GET	Hacker News
/market-dashboard/	GET	Market dashboard
/ai/market-analysis	GET	AI market analysis
/ai-insights/	GET	AI insights
/product-intelligence/analyze	GET	Product analysis
/history/	GET	History
/history/{id}	GET	Single history record
/moodboard/	POST	Moodboard
/gemini-report/	POST	Gemini report
🚀 14. How to Start the Project
Prerequisites

Install:

Python 3.11
Git
Docker Desktop
A Google Gemini API key

Check Python:

python --version

Check Git:

git --version

Check Docker:

docker --version
📥 15. Clone the Repository
git clone https://github.com/sundar66kalyan/AI_Product_Intelligence_Suite.git

Move into the project:

cd AI_Product_Intelligence_Suite
🔐 16. Configure Environment Variables

Create a .env file according to your local configuration.

Example:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

DATABASE_URL=sqlite:///./data/market_intelligence.db

API_BASE_URL=http://localhost:8000

Never commit your real API key to GitHub.

The .env file should remain ignored by Git.

🐍 17. Create Virtual Environment

From the project root:

python -m venv .venv

Activate it:

.venv\Scripts\Activate.ps1

You should see:

(.venv)

in the terminal.

📦 18. Install Backend Dependencies
pip install -r backend\requirements.txt
📦 19. Install Frontend Dependencies
pip install -r frontend\requirements.txt
▶️ 20. Start Backend Locally

From the project root:

uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

Depending on your package configuration, you can alternatively run the backend from the backend directory using its application entry point.

Backend:

http://127.0.0.1:8000
❤️ 21. Test Backend Health

Open:

http://127.0.0.1:8000/health

Expected response:

{
  "status": "healthy"
}
▶️ 22. Start Frontend

Open another PowerShell terminal.

Activate the environment:

cd D:\AI_Product_Intelligence_Suite
.venv\Scripts\Activate.ps1

Then:

streamlit run frontend\app.py

The application should open at:

http://localhost:8501
🐳 23. Start Using Docker

Docker is recommended for reproducing the complete frontend/backend environment.

Build Backend

From project root:

docker build -t ai-product-backend:latest backend
Build Frontend
docker build -t ai-product-frontend:latest frontend
🌐 24. Create Docker Network
docker network create ai-product-network

If the network already exists, Docker will report that it already exists.

▶️ 25. Start Backend Container
docker run -d `
  --name ai-backend `
  --network ai-product-network `
  -p 8000:8000 `
  ai-product-backend:latest

Check:

docker ps
▶️ 26. Start Frontend Container
docker run -d `
  --name ai-frontend `
  --network ai-product-network `
  -p 9000:8501 `
  ai-product-frontend:latest

Check:

docker ps

Expected:

ai-frontend
ai-backend
🔗 27. Test Frontend → Backend Connectivity

This is an important Docker test:

docker run --rm `
  --name ai-frontend-test `
  --network ai-product-network `
  ai-product-frontend:latest `
  python -c "import requests; r=requests.get('http://ai-backend:8000/health'); print(r.status_code); print(r.text)"

Expected:

200
{"status":"healthy", ...}
🌐 28. Open Docker Application

Frontend:

http://localhost:9000

Backend:

http://localhost:8000

Health:

http://localhost:8000/health
📋 29. Useful Docker Commands

Check containers:

docker ps

View backend logs:

docker logs ai-backend

View frontend logs:

docker logs ai-frontend

Follow backend logs:

docker logs -f ai-backend

Check resource usage:

docker stats

Check network:

docker network inspect ai-product-network

Stop frontend:

docker stop ai-frontend

Stop backend:

docker stop ai-backend

Remove frontend:

docker rm -f ai-frontend

Remove backend:

docker rm -f ai-backend
🔧 30. Troubleshooting
Backend cannot start

Check:

docker logs ai-backend
SQLite error

If you see:

sqlite3.OperationalError:
unable to open database file

check:

Database path
/app/data directory
Dockerfile
File permissions
Frontend cannot connect to backend

Inside Docker, don't use:

localhost:8000

Use:

http://ai-backend:8000

because the services communicate through the Docker network.

Container name already exists

If Docker reports:

Conflict. The container name "/ai-backend"
is already in use

check:

docker ps -a

Then remove the old container if appropriate:

docker rm -f ai-backend
🔒 31. Security

Important security practices:

Never commit .env
Never expose GOOGLE_API_KEY
Never hardcode secrets
Use environment variables
Validate API input
Handle external API failures
Avoid exposing internal stack traces
Use HTTPS in production
🧪 32. Testing Strategy

The project should be tested at multiple levels:

Unit Testing
     ↓
API Testing
     ↓
Integration Testing
     ↓
Docker Testing
     ↓
Deployment Testing

Important tests include:

Backend health
API endpoints
Database operations
Gemini integration
Frontend/backend connectivity
Error handling
Docker networking
📈 33. Scalability Roadmap

Current:

Streamlit
+
FastAPI
+
SQLite
+
Gemini
+
Docker

Future production architecture:

Streamlit / React
       ↓
Load Balancer
       ↓
FastAPI
       ↓
Redis
       ↓
PostgreSQL
       ↓
AI Services
       ↓
Gemini / Other LLMs

Additional improvements:

Authentication
Role-based access
PostgreSQL
Redis caching
Background workers
CI/CD
Monitoring
Automated testing
LLM evaluation
Prompt versioning
🎯 34. Learning Outcomes

Through this project, I developed practical experience in:

Python application development
Generative AI
LLM integration
Prompt engineering
FastAPI
REST API development
Streamlit
Data processing
SQLAlchemy
SQLite
Docker
Docker networking
Git/GitHub
Cloud deployment
Debugging production issues
AI application architecture
💼 35. Resume Description
AI Product Intelligence Suite

Python | FastAPI | Streamlit | Gemini | SQLAlchemy | SQLite | Docker | GitHub

Built and deployed an AI-powered product and market intelligence platform combining market trends, news, product intelligence and Gemini-generated strategic insights. Developed modular Streamlit and FastAPI services, implemented analysis history using SQLAlchemy/SQLite, integrated structured LLM responses, containerized frontend/backend services with Docker, and deployed a publicly accessible application.

🎤 36. Interview Explanation
60-Second Project Explanation

"My project is an AI Product Intelligence Suite designed to help users analyze products, markets and competitive opportunities. I built the frontend using Streamlit and the backend using FastAPI. The application collects market and product signals and uses Google Gemini to generate structured insights such as strengths, weaknesses, opportunities and threats. I implemented a service-based architecture with SQLAlchemy and SQLite for analysis history. I containerized the frontend and backend separately using Docker and configured Docker networking between them. During development I solved issues such as SQLite database paths inside containers and localhost versus container networking. The application is now publicly deployed and available through Streamlit."

🧑‍💻 37. Author
Kalyana Sundar

AI / ML Engineer | Generative AI | Python | Data Science

This project demonstrates practical experience in:

AI Engineering
Machine Learning
Generative AI
Backend Development
API Development
Data Engineering
Docker
Cloud Deployment
🌐 38. Project Links
Live Application

https://ai-pro-intelligence-suite-kalyanasundar.streamlit.app/

GitHub Repository

https://github.com/sundar66kalyan/AI_Product_Intelligence_Suite

⭐ 39. Project Highlights
┌────────────────────────────────────────────┐
│       AI PRODUCT INTELLIGENCE SUITE        │
├────────────────────────────────────────────┤
│                                            │
│  🤖 Gemini AI                              │
│  📊 Market Intelligence                   │
│  🔎 Product Intelligence                  │
│  🏆 Competitor Analysis                   │
│  📈 Market Trends                         │
│  📰 News Intelligence                     │
│  🎨 AI Moodboard                          │
│  📄 AI Reports                            │
│  🕘 Analysis History                      │
│  ⚡ FastAPI Backend                        │
│  🎨 Streamlit Frontend                    │
│  🐳 Docker                                │
│  🗄️ SQLAlchemy + SQLite                  │
│  ☁️ Public Deployment                     │
│                                            │
└────────────────────────────────────────────┘
📌 40. Quick Start

For someone who clones the repository:

git clone https://github.com/sundar66kalyan/AI_Product_Intelligence_Suite.git

cd AI_Product_Intelligence_Suite

python -m venv .venv

.venv\Scripts\Activate.ps1

pip install -r backend\requirements.txt

pip install -r frontend\requirements.txt

Configure .env, then start the backend:

uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000

Open another terminal and run:

streamlit run frontend\app.py

Then open:

http://localhost:8501
🚀 Docker Quick Start
docker network create ai-product-network

docker build -t ai-product-backend:latest backend

docker build -t ai-product-frontend:latest frontend

docker run -d --name ai-backend --network ai-product-network -p 8000:8000 ai-product-backend:latest

docker run -d --name ai-frontend --network ai-product-network -p 9000:8501 ai-product-frontend:latest

Open:

http://localhost:9000
📜 License

This project is developed as a personal AI Engineering portfolio project by Kalyana Sundar.

⭐ Final Note

If you found this project useful or interesting, feel free to explore the source code and live application.

Built with Python, FastAPI, Streamlit, Gemini and Docker by Kalyana Sundar.