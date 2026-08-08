import json

from app.database.session import SessionLocal
from app.models.history import History


def save_history(db, analysis_type, title, analysis):

    row = History(
        analysis_type=analysis_type,
        title=title,
        analysis=json.dumps(analysis),   # save complete JSON
    )

    db.add(row)
    db.commit()


def get_all_history():

    db = SessionLocal()

    rows = db.query(History).order_by(
        History.created_at.desc()
    ).all()

    db.close()

    return rows


def delete_history(history_id):

    db = SessionLocal()

    row = db.query(History).filter(
        History.id == history_id
    ).first()

    if row:
        db.delete(row)
        db.commit()

    db.close()