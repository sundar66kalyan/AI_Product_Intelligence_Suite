from pydantic import BaseModel
from datetime import datetime


class ProductCreate(BaseModel):
    product_name: str
    category: str
    source: str


class ProductResponse(BaseModel):
    id: int
    product_name: str
    category: str
    source: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }