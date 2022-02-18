from app.db.fake_data import fake_data
from app.db.init_db import init_db
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    init_db(db)
    fake_data(db)


if __name__ == "__main__":
    init()
