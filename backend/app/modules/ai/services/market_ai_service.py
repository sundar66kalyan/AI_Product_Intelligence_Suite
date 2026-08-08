import json

from app.modules.market.services.aggregator_service import get_market_snapshot
from app.services.llm_service import ask_gemini


def generate_market_report():

    snapshot = get_market_snapshot()

    prompt = f"""
You are a Senior AI Market Intelligence Analyst.

Analyze the following market data.

Return ONLY valid JSON.

Required JSON Format:

{{
    "executive_summary":"",
    "top_trends":[],
    "business_opportunities":[],
    "competitor_insights":[],
    "content_ideas":[],
    "startup_ideas":[],
    "opportunity_score":0,
    "risk_score":0
}}

Market Data:

{json.dumps(snapshot, indent=2)}
"""

    response = ask_gemini(prompt)

    try:
        return json.loads(response)
    except Exception:
        return {
            "raw_response": response
        }