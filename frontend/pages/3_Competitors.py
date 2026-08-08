import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from services.api import analyze_product

st.set_page_config(
    page_title="Competitor Intelligence",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Competitor Intelligence")

# ===============================
# Sidebar
# ===============================

st.sidebar.header("⚙ Analysis Settings")

product_input = st.sidebar.text_input(
    "Competitor Name",
    "ChatGPT"
)

analysis_depth = st.sidebar.select_slider(
    "Analysis Depth",
    options=["Quick", "Standard", "Deep"],
    value="Standard"
)

show_strengths = st.sidebar.checkbox(
    "Show Strengths",
    True
)

show_weaknesses = st.sidebar.checkbox(
    "Show Weaknesses",
    True
)

show_opportunities = st.sidebar.checkbox(
    "Show Opportunities",
    True
)

show_threats = st.sidebar.checkbox(
    "Show Threats",
    True
)

show_executive_summary = st.sidebar.checkbox(
    "Show Executive Summary",
    True
)

show_scores = st.sidebar.checkbox(
    "Show Scores",
    True
)

show_visualizations = st.sidebar.checkbox(
    "Show Visualizations",
    True
)

# Main content area
product = st.text_input(
    "Competitor Name",
    product_input
)

if st.button("Analyze Competitor"):

    with st.spinner(f"Analyzing {product} at {analysis_depth} depth..."):

        data = analyze_product(product)

    if not data:
        st.error("No response from API")
        st.stop()

    st.success("Analysis Complete")

    analysis = data.get("analysis", "")

    # API returns markdown text
    if isinstance(analysis, str):

        st.markdown(analysis)

        # Try to parse as JSON if it looks like JSON
        import json
        try:
            # Check if it's a JSON string
            if analysis.strip().startswith('{') or analysis.strip().startswith('['):
                parsed = json.loads(analysis)
                analysis = parsed
        except:
            pass

    # API returns dictionary
    if isinstance(analysis, dict):

        # Executive Summary
        if show_executive_summary:
            st.header("📋 Executive Summary")
            st.write(analysis.get("executive_summary",""))
            st.divider()

        # Create columns for better layout
        col1, col2 = st.columns(2)
        
        with col1:
            # Strengths
            if show_strengths:
                st.subheader("✅ Strengths")
                strengths = analysis.get("strengths", [])
                
                if isinstance(strengths, list):
                    for s in strengths:
                        st.success(s)
                
                # Add count badge
                st.caption(f"Total: {len(strengths)} strengths identified")
            
            # Opportunities
            if show_opportunities:
                st.subheader("🚀 Opportunities")
                opportunities = analysis.get("opportunities", [])
                
                if isinstance(opportunities, list):
                    for o in opportunities:
                        st.info(o)
                
                st.caption(f"Total: {len(opportunities)} opportunities identified")
        
        with col2:
            # Weaknesses
            if show_weaknesses:
                st.subheader("⚠️ Weaknesses")
                weaknesses = analysis.get("weaknesses", [])
                
                if isinstance(weaknesses, list):
                    for w in weaknesses:
                        st.error(w)
                
                st.caption(f"Total: {len(weaknesses)} weaknesses identified")
            
            # Threats
            if show_threats:
                st.subheader("🔥 Threats")
                threats = analysis.get("threats", [])
                
                if isinstance(threats, list):
                    for t in threats:
                        st.warning(t)
                
                st.caption(f"Total: {len(threats)} threats identified")

        st.divider()

        # Score Section with Charts
        if show_scores:
            st.header("📊 Analysis Scores")

            # Create metrics row
            col1, col2, col3 = st.columns(3)
            
            opportunity_score = analysis.get("opportunity_score", 0)
            risk_score = analysis.get("risk_score", 0)
            
            with col1:
                st.metric(
                    "💡 Opportunity Score",
                    opportunity_score,
                    delta="+2"
                )
            
            with col2:
                st.metric(
                    "⚠️ Risk Score",
                    risk_score,
                    delta="-1"
                )
            
            with col3:
                # Calculate health score (simplified)
                health_score = max(0, min(100, opportunity_score - risk_score + 50))
                
                st.metric(
                    "📈 Health Score",
                    health_score,
                    delta="+5"
                )

        st.divider()

        # Visualizations
        if show_visualizations and isinstance(analysis, dict):
            
            # Create a dataframe for visualization
            chart_data = pd.DataFrame({
                'Category': ['Strengths', 'Weaknesses', 'Opportunities', 'Threats'],
                'Count': [
                    len(analysis.get('strengths', [])),
                    len(analysis.get('weaknesses', [])),
                    len(analysis.get('opportunities', [])),
                    len(analysis.get('threats', []))
                ]
            })
            
            left, right = st.columns(2)
            
            with left:
                fig = px.bar(
                    chart_data,
                    x='Category',
                    y='Count',
                    title='Competitor Analysis Breakdown',
                    color='Category',
                    color_discrete_map={
                        'Strengths': '#00ff00',
                        'Weaknesses': '#ff0000',
                        'Opportunities': '#00bfff',
                        'Threats': '#ffa500'
                    },
                    text='Count'
                )
                fig.update_traces(textposition='outside')
                st.plotly_chart(fig, use_container_width=True)
            
            with right:
                fig2 = px.pie(
                    chart_data,
                    names='Category',
                    values='Count',
                    title='Analysis Distribution',
                    color='Category',
                    color_discrete_map={
                        'Strengths': '#00ff00',
                        'Weaknesses': '#ff0000',
                        'Opportunities': '#00bfff',
                        'Threats': '#ffa500'
                    }
                )
                st.plotly_chart(fig2, use_container_width=True)

            # Download button for analysis
            import json
            
            analysis_json = json.dumps(analysis, indent=2)
            
            st.download_button(
                "📥 Download Analysis Report",
                analysis_json,
                f"{product}_analysis.json",
                "application/json"
            )

    # If analysis is neither string nor dict, just display it
    elif analysis:
        st.write(analysis)