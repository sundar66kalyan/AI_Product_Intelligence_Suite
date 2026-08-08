import streamlit as st
from services.api import analyze_product

st.set_page_config(
    page_title="AI Product Intelligence",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Product Intelligence")

product = st.text_input(
    "Enter Product Name",
    placeholder="ChatGPT"
)

if st.button("Analyze Product"):
    if product:
        with st.spinner("Analyzing..."):
            result = analyze_product(product)
            
            if result and result.get("status") == "success":
                analysis = result["analysis"]
                
                st.success("Analysis Complete")
                
                st.subheader("📋 Executive Summary")
                st.info(analysis["executive_summary"])
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("✅ Strengths")
                    for item in analysis["strengths"]:
                        st.success(item)
                    
                    st.subheader("❌ Weaknesses")
                    for item in analysis["weaknesses"]:
                        st.error(item)
                
                with col2:
                    st.subheader("🚀 Opportunities")
                    for item in analysis["opportunities"]:
                        st.info(item)
                    
                    st.subheader("⚠ Threats")
                    for item in analysis["threats"]:
                        st.warning(item)
                
                c1, c2 = st.columns(2)
                
                with c1:
                    st.metric("Opportunity Score", analysis["opportunity_score"])
                
                with c2:
                    st.metric("Risk Score", analysis["risk_score"])
            else:
                st.error("Analysis failed. Please try again.")
    else:
        st.warning("Please enter a product name")

# Optional: Add example products for quick testing
with st.expander("💡 Example Products to Try"):
    st.write("• ChatGPT")
    st.write("• Tesla Model 3")
    st.write("• Apple iPhone")
    st.write("• Netflix")
    st.write("• Airbnb")