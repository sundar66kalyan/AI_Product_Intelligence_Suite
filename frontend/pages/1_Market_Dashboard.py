import streamlit as st
import pandas as pd

from services.api import get_market_dashboard

st.set_page_config(
    page_title="Market Dashboard",
    layout="wide"
)

st.title("📊 Market Dashboard")

data = get_market_dashboard()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📦 Products", data["total_products"])

with col2:
    st.metric("🔥 Trending", data["trending"])

with col3:
    st.metric("📈 Opportunity", data["opportunity"])

with col4:
    st.metric("⚠ Risk", data["risk"])

st.divider()

# Product Table
st.subheader("Trending Products")

df = pd.DataFrame(data["products"])

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# Chart
st.subheader("Market Leaderboard")

st.bar_chart(
    df.set_index("name")
)