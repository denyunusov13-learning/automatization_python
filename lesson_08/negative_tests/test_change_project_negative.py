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
def get_api_key():
    """
    Шаг 2: подтягиваем ключ из .env
    """
    key = os.getenv("YOUGILE_API_KEY")
    if not key:
        pytest.fail("Не задан YOUGILE_API_KEY в .env! Создай ключ")
    return key


@pytest.fixture
def headers(get_api_key):
    """
    Шаг 3: определяем хэдэры для запроса
    """
    return {
        "Authorization": f"Bearer {get_api_key}",
        "Content-Type": "application/json"
    }


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
