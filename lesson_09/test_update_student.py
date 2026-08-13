from sqlalchemy import text
import pytest


def test_update(connection):
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

    update_sql = text(
        """
        UPDATE student
        SET level = :level, education_form = :education_form
        WHERE user_id = :user_id
        """
    )
    connection.execute(
        update_sql,
        {
            "user_id": 19999,
            "level": "Elementary",
            "education_form": "group",
        },
    )

    check_sql = text(
        "SELECT user_id, level, education_form, subject_id FROM student WHERE user_id = :user_id"
    )
    result = connection.execute(check_sql, {"user_id": 19999})
    row = result.one_or_none()

    assert row is not None
    assert row.level == "Elementary"
    assert row.education_form == "group"
