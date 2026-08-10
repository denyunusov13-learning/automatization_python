import pytest
from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv

load_dotenv()
db_connection_string = "postgresql://postgeeeee:Natasha******0;@localhost:5432/DataBaseXXXXX"
db = create_engine(db_connection_string)


def test_user_max_id():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == "subject"
