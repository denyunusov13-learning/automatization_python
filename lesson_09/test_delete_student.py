from sqlalchemy import text
import pytest


def test_delete(connection):
    insert_sql = text(
        """
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        """
    )
    connection.execute(
        insert_sql,
        {
            "user_id": 19999,
            "level": "Advanced",
            "education_form": "personal",
            "subject_id": 1,
        },
    )

    delete_sql = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(delete_sql, {"user_id": 19999})

    check_sql = text("SELECT user_id FROM student WHERE user_id = :user_id")
    result = connection.execute(check_sql, {"user_id": 19999})
    row = result.one_or_none()

    assert row is None
