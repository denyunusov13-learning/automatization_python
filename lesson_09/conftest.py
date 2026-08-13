from sqlalchemy import create_engine, text
import os
import pytest

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/testdb")

# engine = create_engine(DATABASE_URL, echo=False, future=True)

db_connection_string = "postgresql://postgres:Natasha1091970;@localhost:5432/DataBase_for_learning"
db = create_engine(db_connection_string, echo=False, future=True)

@pytest.fixture
def connection():
    conn = db.connect()
    transaction = conn.begin()
    yield conn
    transaction.rollback()
    conn.close()
