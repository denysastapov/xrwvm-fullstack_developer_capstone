import requests
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

backend_url = os.getenv(
    'backend_url',
    default="http://127.0.0.1:3030"
)

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://127.0.0.1:5050/"
)


def get_request(endpoint, **kwargs):
    request_url = backend_url.rstrip("/") + "/" + endpoint.lstrip("/")
    print("GET from", request_url, kwargs)

    try:
        response = requests.get(request_url, params=kwargs)
        return response.json()
    except Exception as err:
        print(f"GET request error: {err}")
        return []


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url.rstrip("/") + "/analyze/" + quote(text or "")

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Sentiment analyzer error: {err}")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url.rstrip("/") + "/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"POST review error: {err}")
        return {"error": "Network exception occurred"}