import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"


def test_change_project(headers, new_project_id):
    url = f"{BASE_URL}/projects/{new_project_id}"
    body = {"title": "modified in test title"}

    resp = requests.put(url, headers=headers, json=body)
    assert resp.status_code == 200, f"Ожидался 200, получил {resp.status_code}"

    get_resp = requests.get(url, headers=headers)
    get_resp.raise_for_status()
    changed_project = get_resp.json()

    assert changed_project["title"] == "modified in test title", f"Заголовок не обновился: {changed_project.get('title')}"
    assert "id" in changed_project
