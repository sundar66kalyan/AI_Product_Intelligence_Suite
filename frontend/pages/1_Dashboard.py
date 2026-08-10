import os
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from components.cards import opportunity_chart, radar_chart

# Backend configuration with environment variable support
BACKEND = os.getenv(
    "API_BASE_URL",
    "http://ai-backend:8000"
)

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 AI Product Intelligence Dashboard")

# ===============================
# KPI Cards
# ===============================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Products",
    152
)

col2.metric(
    "Competitors",
    63
)

col3.metric(
    "Reports",
    84
)

col4.metric(
    "Avg Opportunity",
    "87%"
)

st.divider()

# ===============================
# Charts Side by Side
# ===============================

left, right = st.columns(2)

with left:
    st.plotly_chart(
        opportunity_chart(),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        radar_chart(),
        use_container_width=True
    )

st.divider()

# ===============================
# AI Ranking & Market Score Gauge
# ===============================

left, right = st.columns(2)

with left:
    st.subheader("🏆 AI Product Ranking")
    
    ranking_data = [
        {"rank": 1, "product": "ChatGPT", "score": 95},
        {"rank": 2, "product": "Gemini", "score": 92},
        {"rank": 3, "product": "Claude", "score": 90},
        {"rank": 4, "product": "Grok", "score": 85},
        {"rank": 5, "product": "Perplexity", "score": 84}
    ]
    
    for item in ranking_data:
        emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"][item["rank"]-1]
        st.markdown(
            f"""
            <div style="
                background: #f0f2f6;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 8px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            ">
                <span style="font-size: 18px; font-weight: bold;">
                    {emoji} {item['product']}
                </span>
                <span style="
                    background: #4CAF50;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-weight: bold;
                ">
                    {item['score']}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

with right:
    st.subheader("📊 Market Opportunity Score")
    
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=87,
            title={"text": "Market Opportunity"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#4CAF50"},
                "steps": [
                    {"range": [0, 50], "color": "#ff4b4b"},
                    {"range": [50, 75], "color": "#ffa500"},
                    {"range": [75, 100], "color": "#4CAF50"}
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.75,
                    "value": 90
                }
            }
        )
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ===============================
# Recent Analyses Cards
# ===============================

st.subheader("📋 Recent Analyses")

col1, col2, col3 = st.columns(3)

recent_products = [
    {"name": "Gemini", "opportunity": 92, "risk": 35},
    {"name": "Grok", "opportunity": 85, "risk": 40},
    {"name": "Claude", "opportunity": 90, "risk": 28}
]

with col1:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
        ">
            <h2 style="margin: 0; color: white;">{recent_products[0]['name']}</h2>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size: 16px; margin: 5px 0;">
                🎯 Opportunity: <strong>{recent_products[0]['opportunity']}</strong>
            </p>
            <p style="font-size: 16px; margin: 5px 0;">
                ⚠️ Risk: <strong>{recent_products[0]['risk']}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
        ">
            <h2 style="margin: 0; color: white;">{recent_products[1]['name']}</h2>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size: 16px; margin: 5px 0;">
                🎯 Opportunity: <strong>{recent_products[1]['opportunity']}</strong>
            </p>
            <p style="font-size: 16px; margin: 5px 0;">
                ⚠️ Risk: <strong>{recent_products[1]['risk']}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 20px;
            border-radius: 12px;
            color: white;
            text-align: center;
        ">
            <h2 style="margin: 0; color: white;">{recent_products[2]['name']}</h2>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size: 16px; margin: 5px 0;">
                🎯 Opportunity: <strong>{recent_products[2]['opportunity']}</strong>
            </p>
            <p style="font-size: 16px; margin: 5px 0;">
                ⚠️ Risk: <strong>{recent_products[2]['risk']}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ===============================
# AI Insights Section
# ===============================

st.subheader("💡 AI Insights")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Gemini demand increased by 12%")
    st.info("ℹ️ Healthcare AI market growing rapidly")
    
with col2:
    st.warning("⚠️ Competition increasing in enterprise AI")
    st.error("❌ High infrastructure costs for AI deployment")

st.divider()

# ===============================
# Sidebar
# ===============================

st.sidebar.header("⚙ Dashboard Filters")

search = st.sidebar.text_input(
    "Search News"
)

news_limit = st.sidebar.slider(
    "Number of Articles",
    5,
    20,
    10
)

show_google = st.sidebar.checkbox(
    "Google Trends",
    True
)

show_rss = st.sidebar.checkbox(
    "RSS News",
    True
)

show_hacker = st.sidebar.checkbox(
    "Hacker News",
    True
)

# -----------------------------
# Backend Status
# -----------------------------
try:
    health = requests.get(f"{BACKEND}/health").json()

    st.sidebar.success("Backend Connected")

    col1, col2, col3 = st.columns(3)

    col1.metric("Status", health["status"])
    col2.metric("Service", "Backend")
    col3.metric("Version", "1.0")

except Exception:
    st.sidebar.error("Backend Offline")
    st.stop()

st.divider()

# -----------------------------
# Load APIs
# -----------------------------
snapshot = requests.get(f"{BACKEND}/market/snapshot").json()["data"]

google = snapshot["google_trends"]
rss = snapshot["rss_news"]
hacker = snapshot["hacker_news"]

# -----------------------------
# Metrics
# -----------------------------

st.subheader("📈 Market Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🔥 Google Trends",
        len(google),
        delta="+3"
    )

with col2:
    st.metric(
        "📰 RSS News",
        len(rss),
        delta="+7"
    )

with col3:
    st.metric(
        "💻 Hacker News",
        len(hacker),
        delta="+2"
    )

st.divider()

left, right = st.columns(2)

with left:

    chart_df = pd.DataFrame({
        "Source": [
            "Google",
            "RSS",
            "Hacker"
        ],
        "Count": [
            len(google),
            len(rss),
            len(hacker)
        ]
    })

    fig = px.bar(
        chart_df,
        x="Source",
        y="Count",
        title="Market Data Sources"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig2 = px.pie(
        chart_df,
        names="Source",
        values="Count",
        title="Data Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# -----------------------------
# Google Trends
# -----------------------------

if show_google:

    st.subheader("🔥 Google Trends")

    df = pd.DataFrame(
        {
            "Trending Search": google
        }
    )

    st.dataframe(df, use_container_width=True)
    
    csv = df.to_csv(index=False)
    
    st.download_button(
        "📥 Download Google Trends",
        csv,
        "google_trends.csv",
        "text/csv"
    )

    st.divider()

# -----------------------------
# RSS News
# -----------------------------

if show_rss:

    st.subheader("📰 Latest Tech News")

    for article in rss[:news_limit]:
        
        if search.lower() not in article["title"].lower():
            continue

        st.markdown(
            f"""
### {article['title']}

**Source:** {article['source']}

{article['link']}

---
"""
        )

    st.divider()

# -----------------------------
# Hacker News
# -----------------------------

if show_hacker:

    st.subheader("💻 Hacker News")

    for article in hacker[:news_limit]:
        
        if search.lower() not in article["title"].lower():
            continue

        st.markdown(
            f"""
### {article['title']}

⭐ {article['points']} points

{article['url']}

---
"""
        )