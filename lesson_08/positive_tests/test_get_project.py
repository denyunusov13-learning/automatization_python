import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"


def test_get_project(headers, new_project_id):
    url = f"{BASE_URL}/projects/{new_project_id}"
    body = {"title": "modified in test title"}

    resp = requests.get(url, headers=headers, json=body)
    assert resp.status_code == 200, f"Ожидался 200, получил {resp.status_code}"

    received_project = resp.json()

    assert len(received_project) > 0
