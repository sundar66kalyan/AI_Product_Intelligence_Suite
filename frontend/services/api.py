import os
import requests

BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://ai-backend:8000"
)

API_URL = BASE_URL

def get_health():
    response = requests.get(f"{BASE_URL}/health")
    return response.json()


def get_market_snapshot():
    response = requests.get(f"{BASE_URL}/market/snapshot")
    return response.json()


def get_market_analysis():
    response = requests.get(f"{BASE_URL}/ai/market-analysis")
    return response.json()


def get_google_trends():
    response = requests.get(f"{BASE_URL}/market/google-trends")
    return response.json()


def get_latest_news():
    response = requests.get(f"{BASE_URL}/market/news")
    return response.json()


def get_hacker_news():
    response = requests.get(f"{BASE_URL}/market/hacker-news")
    return response.json()


def analyze_product(product):
    response = requests.get(
        f"{BASE_URL}/product-intelligence/analyze",
        params={
            "product": product
        }
    )
    return response.json()


def get_ai_market_analysis():
    response = requests.get(
        f"{BASE_URL}/ai/market-analysis"
    )
    return response.json()


def get_history():
    response = requests.get(f"{BASE_URL}/history/")
    response.raise_for_status()
    return response.json()


def get_history_item(history_id):
    response = requests.get(
        f"{BASE_URL}/history/{history_id}"
    )
    response.raise_for_status()
    return response.json()


def get_market_dashboard():
    response = requests.get(
        f"{BASE_URL}/market-dashboard/"
    )
    response.raise_for_status()
    return response.json()

def get_ai_insights():
    response = requests.get(f"{API_URL}/ai-insights/")
    response.raise_for_status()
    return response.json()