import os
import requests
import pytest
from dotenv import load_dotenv


base_url = "https://ru.yougile.com/api-v2/"
load_dotenv()

@pytest.fixture(scope="session")
def company_id():
    """
    Шаг 1: получаем company_id из переменных окружения.
    """
    comp_id = os.getenv("YOUGILE_COMPANY_ID")
    if not comp_id:
        pytest.fail("Не задан YOUGILE_COMPANY_ID в .env или переменных окружения!")
    print(f"[INFO] Используем company_id: {comp_id}")
    return comp_id

def get_company_id():
    resp = requests.post(base_url+"auth/companies")
    company_id = resp.json()[content]["id"]

def test_project():
    resp = requests.get(base_url+)
