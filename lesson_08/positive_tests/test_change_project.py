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


@pytest.fixture
def new_project_id(headers):
    """
    Шаг 4: получаем и сохраняем в поле последнее id
    """
    resp = requests.get(f"{BASE_URL}/projects", headers=headers)
    resp.raise_for_status()
    new_comp_id = resp.json()["content"][-1]["id"]
    return new_comp_id


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
