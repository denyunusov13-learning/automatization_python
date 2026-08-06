import requests
import pytest


BASE_URL = "https://ru.yougile.com/api-v2"


def test_change_project(headers, new_project_id=234234234234):
    """
    намеренно подставляем несуществующий id
    """
    url = f"{BASE_URL}/projects/{new_project_id}"
    body = {"title": "modified in test title"}

    resp = requests.put(url, headers=headers, json=body)

    assert resp.status_code == 404, f"Ожидалась ошибка 404, получил {resp.status_code}"
    error_body = resp.json()
    assert "message" in error_body or "error" in error_body
