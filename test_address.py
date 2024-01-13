import pytest
import requests
from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI
import json

app = FastAPI()

client = TestClient(app,base_url="http://127.0.0.1:8000/v1")

user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQxNjg5NDE1ZWMyM2EzMzdlMmJiYWE1ZTNlNjhiNjZkYzk5MzY4ODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWlzZnQtZWFzLTliYmRlIiwiYXVkIjoiYWlzZnQtZWFzLTliYmRlIiwiYXV0aF90aW1lIjoxNzA1MTczMjg5LCJ1c2VyX2lkIjoibkF6UVlkTkJ5bVRDYUxkWkVXZTM1dFdBUEI4MyIsInN1YiI6Im5BelFZZE5CeW1UQ2FMZFpFV2UzNXRXQVBCODMiLCJpYXQiOjE3MDUxNzMyODksImV4cCI6MTcwNTE3Njg4OSwiZW1haWwiOiJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.LUkbgrulAh9dEeLG4UyJfjYpiH-k2kqPMlsncmLJnCk4xsFyrjjAdQaGk8IFUCN3IxCPjZaP8irid31z65tcHBuPkyKbrviTIa9wDOCqxrIKibqNeXj9fM1xMYKTP59tssVn3TQXAjg81z4U4gjAJC2kiAJqOtypIWGBswxbA9c4_p808vAs8R5Kqb8um5xFHwVE6YM7c6MuWxDVf6ViDinKrnOCWMODzVjDzzsvY-p-K0ziy8gqA37jsg91LDe6ntowYTIbYBd5vaDP2C7tOycarFvTPjRKzC1PSIcFtBO71YEN9PnNY3RiS37ertPxO42yjuO3wM5rtwjHJKDM3w"
add_payload = {
  "add_line_1": "Mahatma Gandhi Road",
  "add_line_2": "Ward No 1",
  "city": "Nagpur",
  "zip_code": "441501",
  "email": "abc@gmail.com",
  "phone_no": 9876543282,
  "country": "India",
  "state": "Maharashtra",
  "address_type": True
}

def test_create_general_ledger():
    response = requests.post("http://127.0.0.1:8000/v1/address", params={"user_token": user_token},
        data=json.dumps(add_payload)
    )
    assert response.status_code == 200

    add_data = response.json()
    assert add_data["add_line_1"] == "Mahatma Gandhi Road"
    assert add_data["add_line_2"] == "Ward No 1"
    assert add_data["city"] == "Nagpur"
    assert add_data["zip_code"] == "441501"
    assert add_data["email"] == "abc@gmail.com"
    assert add_data["phone_no"] == 9876543282
    assert add_data["country"] == "India"
    assert add_data["state"] == "Maharashtra"
    assert add_data["address_type"] == True
