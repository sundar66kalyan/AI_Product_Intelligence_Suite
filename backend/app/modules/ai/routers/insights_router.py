from fastapi import APIRouter

router = APIRouter(
    prefix="/ai-insights",
    tags=["AI Insights"]
)

@router.get("/")
def get_ai_insights():

    return {
        "summary": "The AI market is experiencing rapid growth, led by generative AI products.",
        "opportunities": [
            "Enterprise AI adoption is increasing.",
            "AI copilots are gaining popularity.",
            "Healthcare AI demand is growing."
        ],
        "risks": [
            "Strong competition among AI vendors.",
            "High infrastructure costs.",
            "Regulatory uncertainty."
        ],
        "recommendations": [
            "Invest in enterprise solutions.",
            "Focus on AI automation.",
            "Monitor competitor launches."
        ]
    }