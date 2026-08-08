import streamlit as st
from services.api import get_health

st.set_page_config(
    page_title="AI Product Intelligence Suite",
    page_icon="🚀",
    layout="wide"
)

# ===============================
# Hero Section
# ===============================

st.title("🚀 KalyanaSundar AI Solutions")

st.subheader("AI Product Intelligence Suite")

st.success(
    """
    Enterprise AI platform for Product Intelligence,
    Competitor Analysis,
    Market Research,
    AI Insights,
    Executive Reporting,
    and Strategic Decision Making.
    """
)

st.markdown("---")

# ===============================
# Developer Info
# ===============================

st.markdown("""
### 👨‍💻 Developed By

**Kalyana Sundar**

AI Engineer | Machine Learning Engineer | Data Scientist

📍 India

⭐ [GitHub](https://github.com/sundar66kalyan/AI_Product_Intelligence_Suite)

🌐 [Portfolio](https://kalyanasundarportfolioaiengineer.netlify.app/)

📧 [Contact](mailto:kalyanasundar@example.com)
""")

st.markdown("---")

# ===============================
# What is this Application?
# ===============================

st.header("📖 What is this Application?")

st.write("""
AI Product Intelligence Suite is an AI-powered enterprise platform designed to help businesses, 
startups, investors, and product teams analyze products using Large Language Models (LLMs).

It combines multiple AI agents into a single application that can:

- Analyze products
- Discover market trends
- Monitor competitors
- Generate executive reports
- Create visual moodboards
- Identify business opportunities
- Assess risks
- Support strategic business decisions

Instead of manually collecting information from multiple websites, the platform uses AI to 
generate actionable insights within seconds.
""")

st.markdown("---")

# ===============================
# Why was this built?
# ===============================

st.header("🎯 Why was this Built?")

st.write("""
Modern companies launch thousands of products every year.

Businesses struggle to answer questions like:

- Is this product worth investing in?
- Who are its competitors?
- What are its strengths?
- What risks exist?
- Is there market demand?
- What design trends should we follow?
- What business opportunities exist?

This platform automates those tasks using AI.
""")

st.markdown("---")

# ===============================
# Problems Solved
# ===============================

st.header("🚀 Problems Solved")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ❌ Traditional Approach
    - Reading hundreds of articles
    - Searching Google manually
    - Comparing competitors manually
    - Writing reports
    - Researching design inspiration
    """)

with col2:
    st.markdown("""
    ### ✅ AI-Powered Solution
    - Product Intelligence
    - SWOT Analysis
    - Executive Reports
    - Competitor Insights
    - Market Trends
    - AI Recommendations
    """)

st.markdown("---")

# ===============================
# Core Features
# ===============================

st.header("✨ Core Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🔍 Product Search**
    Analyze any product using AI
    
    **📊 AI Insights**
    Executive summary and SWOT
    """)

with col2:
    st.markdown("""
    **🏢 Competitor Analysis**
    Compare competing products
    
    **📈 Market Trends**
    Google Trends + AI News
    """)

with col3:
    st.markdown("""
    **📋 Dashboard**
    Live analytics dashboard
    
    **🎨 Moodboard**
    Generate branding inspiration
    """)

st.markdown("---")

# ===============================
# Application Workflow
# ===============================

st.header("⚙ Application Workflow")

workflow_steps = [
    "User",
    "Enter Product",
    "AI Product Analysis",
    "Competitor Research",
    "Market Trends",
    "SWOT Analysis",
    "Opportunity Score",
    "Risk Score",
    "Executive Report",
    "Moodboard",
    "Decision Making"
]

for step in workflow_steps:
    st.markdown(f"⬇️ **{step}**")

st.markdown("---")

# ===============================
# Technology Stack
# ===============================

st.header("🛠 Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Frontend")
    st.markdown("""
    - Streamlit
    - Plotly
    - Pandas
    """)

with col2:
    st.subheader("Backend")
    st.markdown("""
    - FastAPI
    - SQLite
    - REST API
    """)

with col3:
    st.subheader("AI")
    st.markdown("""
    - Gemini
    - LLM
    - Prompt Engineering
    """)

with col4:
    st.subheader("Data & Visualization")
    st.markdown("""
    - Google Trends
    - AI News
    - Competitor Analysis
    - Plotly Charts
    - Radar Charts
    - Dashboards
    """)

st.markdown("---")

# ===============================
# Business Use Cases
# ===============================

st.header("💼 Business Use Cases")

use_cases = {
    "Startups": "Product validation",
    "Investors": "Investment research",
    "Product Managers": "Competitor tracking",
    "Marketing Teams": "Market intelligence",
    "Sales Teams": "Product positioning",
    "Executives": "Strategic decisions"
}

for industry, use_case in use_cases.items():
    st.markdown(f"**{industry}** → {use_case}")

st.markdown("---")

# ===============================
# Architecture
# ===============================

st.header("🏗 Architecture")

st.code("""
                User
                   │
            Streamlit UI
                   │
              FastAPI API
                   │
      -------------------------
      Product Agent
      Market Agent
      Competitor Agent
      Moodboard Agent
      Gemini Report Agent
      -------------------------
                   │
              Gemini LLM
                   │
          Structured Output
                   │
         Dashboard + Reports
""", language="text")

st.markdown("---")

# ===============================
# How to Use
# ===============================

st.header("📚 How to Use")

steps = [
    "Open Dashboard",
    "Search Product",
    "Analyze Product",
    "View SWOT Analysis",
    "Check Market Trends",
    "Compare Competitors",
    "Generate Moodboard",
    "Generate Executive Report",
    "Make Business Decision"
]

for i, step in enumerate(steps, 1):
    st.markdown(f"**Step {i}** → {step}")

st.markdown("---")

# ===============================
# Why is this Project Different?
# ===============================

st.header("🏆 Why This Project is Unique")

st.write("""
Unlike a normal chatbot, this platform combines multiple AI capabilities into one enterprise application:

- AI Product Intelligence
- Competitor Intelligence
- Market Research
- Executive Reporting
- AI Moodboard Generation
- Business Dashboard
- Google Trends Analysis
- Opportunity Scoring
- Risk Assessment
- Interactive Data Visualizations

This makes it a comprehensive AI product strategy platform rather than a single-purpose AI demo.
""")

st.markdown("---")

# ===============================
# About the Developer
# ===============================

st.header("👨‍💻 About the Developer")

st.write("""
**Kalyana Sundar**

AI Engineer focused on building practical AI applications that solve real business problems.

Areas of expertise:

- Machine Learning
- Generative AI
- LLM Applications
- FastAPI
- Streamlit
- Product Intelligence
- NLP
- Computer Vision
""")

st.markdown("---")

# ===============================
# Backend Status (Footer)
# ===============================

try:
    health = get_health()
    st.success("✅ Backend Connected Successfully")
except Exception as e:
    st.error("❌ Cannot connect to FastAPI Backend")
    st.exception(e)