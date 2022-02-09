from app.api.deps import SessionLocal


def init() -> None:
    db = SessionLocal()
    init_db(db)