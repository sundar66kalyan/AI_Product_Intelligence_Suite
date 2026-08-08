from fastapi import APIRouter

router = APIRouter(prefix="/market-dashboard", tags=["Market Dashboard"])


@router.get("/")
def dashboard():

    return {
        "total_products": 120,
        "trending": 25,
        "opportunity": 84,
        "risk": 30,
        "products":[
            {"name":"ChatGPT","score":98},
            {"name":"Claude","score":91},
            {"name":"Gemini","score":90},
            {"name":"Perplexity","score":88},
            {"name":"Cursor","score":87}
        ]
    }