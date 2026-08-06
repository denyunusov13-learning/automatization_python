import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"


def test_create_project(headers, company_id):
    url = f"{BASE_URL}/projects"
    params = {"companyId": company_id}
    body = {"title": "penal enforcement inspectorate"}

    resp = requests.post(url, headers=headers, params=params, json=body)

    assert resp.status_code == 201, f"Ожидался 201, получил {resp.status_code}"
    project = resp.json()
    assert "id" in project
