from fastapi import APIRouter

router = APIRouter(
    prefix="/moodboard",
    tags=["Moodboard"]
)

@router.post("/")
def generate_moodboard(data: dict):

    prompt = data.get("prompt", "")

    return {
        "title": prompt,
        "style": "Modern AI SaaS",
        "colors": [
            "#4F46E5",
            "#06B6D4",
            "#10B981",
            "#F59E0B",
            "#EF4444"
        ],
        "fonts": [
            "Inter",
            "Poppins"
        ],
        "keywords": [
            "Minimal",
            "Glassmorphism",
            "Gradient",
            "Dark UI"
        ]
    }