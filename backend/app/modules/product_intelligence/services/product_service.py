from app.services.history_service import save_history
from app.services.llm_service import ask_gemini
from app.database.session import SessionLocal
import json


def analyze_product(product_name: str):

    prompt = f"""
You are a Senior Product Manager.

Analyze this product:

{product_name}

Provide:

1. Product Summary
2. Key Features
3. Target Audience
4. Competitors
5. Strengths
6. Weaknesses
7. Opportunities
8. Threats
9. Market Demand
10. Future Prediction

Return ONLY valid JSON.

Use exactly this format.

{{
  "executive_summary":"",

  "strengths":[
      "",
      "",
      ""
  ],

  "weaknesses":[
      "",
      "",
      ""
  ],

  "opportunities":[
      "",
      "",
      ""
  ],

  "threats":[
      "",
      "",
      ""
  ],

  "opportunity_score":85,

  "risk_score":20
}}

Do NOT write markdown.

Do NOT use code fences.

Do NOT explain anything.

Return JSON only.
"""

    response = ask_gemini(prompt)

    print("\n===== GEMINI RESPONSE =====")
    print(response)
    print("===========================\n")

    # Clean response - remove code fences if present
    response = response.strip()

    if response.startswith("```json"):
        response = response.replace("```json", "", 1)

    if response.startswith("```"):
        response = response.replace("```", "", 1)

    response = response.replace("```", "").strip()

    try:
        analysis = json.loads(response)
    except json.JSONDecodeError:
        analysis = {
            "executive_summary": response,
            "strengths": [],
            "weaknesses": [],
            "opportunities": [],
            "threats": [],
            "opportunity_score": 0,
            "risk_score": 0,
        }
    
    db = SessionLocal()
    
    try:
        save_history(
            db=db,
            analysis_type="Product",
            title=product_name,
            analysis=analysis,
        )
    finally:
        db.close()
    
    return analysis