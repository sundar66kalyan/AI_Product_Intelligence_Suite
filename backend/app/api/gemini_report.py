from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/gemini-report", tags=["Gemini Report"])


class ReportRequest(BaseModel):
    product: str


@router.post("/")
def generate_report(request: ReportRequest):

    return {
        "executive_summary":
            f"{request.product} is an AI product with high market potential and increasing enterprise adoption.",

        "strengths": [
            "Strong AI capabilities",
            "Growing user adoption",
            "Enterprise-ready architecture"
        ],

        "weaknesses": [
            "High infrastructure costs",
            "Strong competition",
            "Rapid technology changes"
        ],

        "opportunities": [
            "Healthcare",
            "Finance",
            "Education",
            "Retail"
        ],

        "risks": [
            "Competition from OpenAI",
            "Regulation",
            "Model hallucinations"
        ],

        "recommendations": [
            "Focus on enterprise customers",
            "Improve integrations",
            "Reduce inference cost",
            "Expand globally"
        ],

        "score": 92
    }