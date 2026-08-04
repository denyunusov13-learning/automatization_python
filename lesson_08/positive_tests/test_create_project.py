import os
import requests
import pytest
from dotenv import load_dotenv

BASE_URL = "https://ru.yougile.com/api-v2"
load_dotenv()


@pytest.fixture(scope="session")
def company_id():
    """
    Шаг 1: получаем company_id из переменных окружения
    """
    comp_id = os.getenv("YOUGILE_COMPANY_ID")
    if not comp_id:
        pytest.fail("Не задан YOUGILE_COMPANY_ID в .env!")
    print(f"[INFO] Используем company_id: {comp_id}")
    return comp_id


@pytest.fixture
def get_api_key(company_id):
    """
    Шаг 2: получаем API-ключ через логин/пароль
    """
    login = os.getenv("YOUGILE_LOGIN")
    password = os.getenv("YOUGILE_PASSWORD")

    body = {
        "login": login,
        "password": password,
        "companyId": company_id
    }

    resp = requests.post(f"{BASE_URL}/auth/keys", json=body)
    resp.raise_for_status()
    key_api = resp.json().get("key")
    return key_api


@pytest.fixture
def headers(get_api_key):
    """
    Шаг 3: определяем хэдэры для запроса
    """
    return {
        "Authorization": f"Bearer {get_api_key}",
        "Content-Type": "application/json"
    }


def test_create_project(headers, company_id):
    url = f"{BASE_URL}/projects"
    params = {"companyId": company_id}
    body = {"title": "penal enforcement inspectorate"}

    resp = requests.post(url, headers=headers, params=params, json=body)

    assert resp.status_code == 201, f"Ожидался 201, получил {resp.status_code}"
    project = resp.json()
    assert "id" in project
