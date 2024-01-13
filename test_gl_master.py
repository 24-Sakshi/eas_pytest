import pytest
import requests
from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI
import json

app = FastAPI()

client = TestClient(app,base_url="http://127.0.0.1:8000/v1")

user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQxNjg5NDE1ZWMyM2EzMzdlMmJiYWE1ZTNlNjhiNjZkYzk5MzY4ODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWlzZnQtZWFzLTliYmRlIiwiYXVkIjoiYWlzZnQtZWFzLTliYmRlIiwiYXV0aF90aW1lIjoxNzA1MTczMjg5LCJ1c2VyX2lkIjoibkF6UVlkTkJ5bVRDYUxkWkVXZTM1dFdBUEI4MyIsInN1YiI6Im5BelFZZE5CeW1UQ2FMZFpFV2UzNXRXQVBCODMiLCJpYXQiOjE3MDUxNzMyODksImV4cCI6MTcwNTE3Njg4OSwiZW1haWwiOiJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.LUkbgrulAh9dEeLG4UyJfjYpiH-k2kqPMlsncmLJnCk4xsFyrjjAdQaGk8IFUCN3IxCPjZaP8irid31z65tcHBuPkyKbrviTIa9wDOCqxrIKibqNeXj9fM1xMYKTP59tssVn3TQXAjg81z4U4gjAJC2kiAJqOtypIWGBswxbA9c4_p808vAs8R5Kqb8um5xFHwVE6YM7c6MuWxDVf6ViDinKrnOCWMODzVjDzzsvY-p-K0ziy8gqA37jsg91LDe6ntowYTIbYBd5vaDP2C7tOycarFvTPjRKzC1PSIcFtBO71YEN9PnNY3RiS37ertPxO42yjuO3wM5rtwjHJKDM3w"
payload = {
        "company_id": 1,
        "rgp_desc_id": 100,
        "gl_display": "100-100",
        "description": "gl description",
        "control": 0,
        "bank_account": 0
    }

def test_create_general_ledger():
    response = requests.post("http://127.0.0.1:8000/v1/general_ledgers", params={"user_token": user_token},
        data=json.dumps(payload)
    )
    assert response.status_code == 200

    gl_data = response.json()
    assert gl_data["company_id"] == 1
    assert gl_data["rgp_desc_id"] == 100
    assert gl_data["gl_display"] == "100-100"
    assert gl_data["description"] == "gl description"
    assert gl_data["control"] == 0
    assert gl_data["bank_account"] == 0
