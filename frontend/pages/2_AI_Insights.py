import streamlit as st
from services.api import get_ai_market_analysis, get_ai_insights

st.set_page_config(
    page_title="AI Insights",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Market Insights")

# Create tabs for different analysis views
tab1, tab2 = st.tabs(["📊 Market Analysis", "🎯 Quick Insights"])

# Tab 1: Full Market Analysis (with button)
with tab1:
    if st.button("Generate AI Insights", key="generate_analysis"):
        with st.spinner("Analyzing Market..."):
            result = get_ai_market_analysis()

        analysis = result.get("analysis", {})

        st.success("Analysis Complete")

        # If analysis is a string representation of a dictionary
        if isinstance(analysis, str):
            import ast
            try:
                analysis = ast.literal_eval(analysis)
            except Exception:
                st.markdown(analysis)
                st.stop()

        # Executive Summary
        if "executive_summary" in analysis:
            st.header("📌 Executive Summary")
            st.write(analysis["executive_summary"])

        # Top Trends
        if "top_trends" in analysis:
            st.header("📈 Top Trends")
            for trend in analysis["top_trends"]:
                st.markdown(f"• {trend}")

        # Business Opportunities
        if "business_opportunities" in analysis:
            st.header("💡 Business Opportunities")
            for item in analysis["business_opportunities"]:
                st.markdown(f"• {item}")

        # Competitor Insights
        if "competitor_insights" in analysis:
            st.header("🏢 Competitor Insights")
            for item in analysis["competitor_insights"]:
                st.markdown(f"• {item}")

        # Startup Ideas
        if "startup_ideas" in analysis:
            st.header("🚀 Startup Ideas")
            for item in analysis["startup_ideas"]:
                st.markdown(f"• {item}")

        # Scores
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Opportunity Score",
                analysis.get("opportunity_score", 0)
            )

        with col2:
            st.metric(
                "Risk Score",
                analysis.get("risk_score", 0)
            )
    else:
        st.info("👆 Click the button above to generate AI market insights")

# Tab 2: Quick AI Insights (auto-loads)
with tab2:
    try:
        data = get_ai_insights()
        
        st.subheader("Executive Summary")
        st.info(data.get("summary", "No summary available"))
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 Opportunities")
            opportunities = data.get("opportunities", [])
            if opportunities:
                for item in opportunities:
                    st.success(item)
            else:
                st.info("No opportunities identified")
        
        with col2:
            st.subheader("⚠ Risks")
            risks = data.get("risks", [])
            if risks:
                for item in risks:
                    st.warning(item)
            else:
                st.info("No risks identified")
        
        st.subheader("💡 Recommendations")
        recommendations = data.get("recommendations", [])
        if recommendations:
            for item in recommendations:
                st.write("✅", item)
        else:
            st.info("No recommendations available")
            
    except Exception as e:
        st.error(f"Error loading quick insights: {str(e)}")
        st.info("Please make sure the API server is running")

# Optional: Add refresh button for quick insights
if st.button("🔄 Refresh All Insights"):
    st.rerun()