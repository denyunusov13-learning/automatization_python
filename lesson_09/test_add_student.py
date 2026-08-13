from sqlalchemy import text
import pytest


def test_insert(connection):
    sql = text(
        """
        INSERT INTO student (user_id, level, education_form, subject_id)
        VALUES (:user_id, :level, :education_form, :subject_id)
        """
    )
    connection.execute(
        sql,
        {
            "user_id": 19999,
            "level": "Advanced",
            "education_form": "personal",
            "subject_id": 1,
        },
    )

    check_sql = text(
        "SELECT user_id, level, education_form, subject_id FROM student WHERE user_id = :user_id"
    )
    result = connection.execute(check_sql, {"user_id": 19999})
    row = result.one_or_none()

    assert row is not None
    assert row.user_id == 19999
    assert row.level == "Advanced"
    assert row.education_form == "personal"
    assert row.subject_id == 1
