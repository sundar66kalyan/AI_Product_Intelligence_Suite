import streamlit as st
import pandas as pd
import plotly.express as px

from services.api import get_market_snapshot

st.set_page_config(
    page_title="Market Trends",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Market Trends")

if st.button("Refresh Trends"):

    data = get_market_snapshot()

    google = data["data"]["google_trends"]
    rss = data["data"]["rss_news"]
    hacker = data["data"]["hacker_news"]

    st.success("Latest market data loaded")

    # -------------------------
    # Google Trends
    # -------------------------

    st.header("🔥 Google Trends")

    df_google = pd.DataFrame(
        {"Trend": google}
    )

    st.dataframe(
        df_google,
        use_container_width=True
    )

    # -------------------------
    # RSS News
    # -------------------------

    st.header("📰 RSS News")

    for article in rss:

        with st.expander(article["title"]):

            st.write("Source:", article["source"])

            st.write(article["link"])

    # -------------------------
    # Hacker News
    # -------------------------

    st.header("💻 Hacker News")

    scores = []

    titles = []

    for item in hacker:

        titles.append(item["title"][:40])

        scores.append(item["points"])

    chart = px.bar(
        x=titles,
        y=scores,
        labels={
            "x":"Article",
            "y":"Points"
        },
        title="Top HackerNews Stories"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )