from sqlalchemy import text
from app.db import get_engine

with get_engine().connect() as conn:
    print("SELECT 1 - >", conn.execute(text("SELECT 1")).scalar())
    print(conn.execute(text("SELECT version()")).scalar())