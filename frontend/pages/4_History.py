import streamlit as st
import pandas as pd

from services.api import (
    get_history,
    get_history_item
)

st.title("📜 Analysis History")

history = get_history()

if history:

    df = pd.DataFrame(history)

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.divider()

    titles = {
        f"{row['id']} - {row['title']}": row["id"]
        for row in history
    }

    selected = st.selectbox(
        "Select Analysis",
        titles.keys()
    )

    if st.button("View Report"):

        report = get_history_item(
            titles[selected]
        )

        st.subheader(report["title"])

        st.json(report["analysis"])

else:

    st.info("No history available.")