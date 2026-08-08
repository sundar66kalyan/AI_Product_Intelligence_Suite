from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.history import History

router = APIRouter(prefix="/history", tags=["History"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_history(db: Session = Depends(get_db)):
    rows = (
        db.query(History)
        .order_by(History.created_at.desc())
        .all()
    )

    return [
        {
            "id": row.id,
            "type": row.analysis_type,
            "title": row.title,
            "created_at": row.created_at,
        }
        for row in rows
    ]


@router.get("/{history_id}")
def get_history_item(history_id: int, db: Session = Depends(get_db)):

    row = db.query(History).filter(
        History.id == history_id
    ).first()

    if row is None:
        return {"error": "Not Found"}

    import json

    return {
        "id": row.id,
        "title": row.title,
        "type": row.analysis_type,
        "analysis": json.loads(row.analysis),
        "created_at": row.created_at,
    }