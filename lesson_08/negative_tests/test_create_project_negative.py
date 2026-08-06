import requests
import pytest


BASE_URL = "https://ru.yougile.com/api-v2"


def test_create_project_negative(headers, company_id):
    url = f"{BASE_URL}/projects"
    params = {"companyId": company_id}
    body = {"title": ""}

    resp = requests.post(url, headers=headers, params=params, json=body)

    assert resp.status_code in (400, 422), f"Ожидалась ошибка валидации, получил {resp.status_code}"
    error_body = resp.json()
    assert "message" in error_body or "error" in error_body
