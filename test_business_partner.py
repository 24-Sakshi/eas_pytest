import pytest
import requests
from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI
import json

app = FastAPI()

client = TestClient(app,base_url="http://127.0.0.1:8000/v1")

user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQxNjg5NDE1ZWMyM2EzMzdlMmJiYWE1ZTNlNjhiNjZkYzk5MzY4ODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWlzZnQtZWFzLTliYmRlIiwiYXVkIjoiYWlzZnQtZWFzLTliYmRlIiwiYXV0aF90aW1lIjoxNzA1MTczMjg5LCJ1c2VyX2lkIjoibkF6UVlkTkJ5bVRDYUxkWkVXZTM1dFdBUEI4MyIsInN1YiI6Im5BelFZZE5CeW1UQ2FMZFpFV2UzNXRXQVBCODMiLCJpYXQiOjE3MDUxNzMyODksImV4cCI6MTcwNTE3Njg4OSwiZW1haWwiOiJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.LUkbgrulAh9dEeLG4UyJfjYpiH-k2kqPMlsncmLJnCk4xsFyrjjAdQaGk8IFUCN3IxCPjZaP8irid31z65tcHBuPkyKbrviTIa9wDOCqxrIKibqNeXj9fM1xMYKTP59tssVn3TQXAjg81z4U4gjAJC2kiAJqOtypIWGBswxbA9c4_p808vAs8R5Kqb8um5xFHwVE6YM7c6MuWxDVf6ViDinKrnOCWMODzVjDzzsvY-p-K0ziy8gqA37jsg91LDe6ntowYTIbYBd5vaDP2C7tOycarFvTPjRKzC1PSIcFtBO71YEN9PnNY3RiS37ertPxO42yjuO3wM5rtwjHJKDM3w"

#to create a business partner type
bpt_payload = {
        
    "company_id": 1,
    "description": "BPT Master 1",
    "gl_id": 1,
    "customer_vendor": True

    }

def test_create_bpt_master():
    response = requests.post("http://127.0.0.1:8000/v1/business_partner_types", params={"user_token": user_token},
        data=json.dumps(bpt_payload)
    )
    assert response.status_code == 200

    bpt_data = response.json()
    assert bpt_data["company_id"] == 1
    assert bpt_data["description"] == "BPT Master 1"
    assert bpt_data["gl_id"] == 1
    assert bpt_data["customer_vendor"] == True


#to create a business partner
bp_payload = {
  "company_id": 1,
  "bp_name": "BP1",
  "bpt_id": 1,
  "payment_term_id": 1,
  "ten99": True,
  "fedralid": "232464",
  "bp_ud_print": "string",
  "contact_person": "string"
}

def test_create_bpt_master():
    response = requests.post("http://127.0.0.1:8000/v1/business_partners", params={"user_token": user_token},
        data=json.dumps(bp_payload)
    )
    assert response.status_code == 200

    bp_data = response.json()
    assert bp_data["company_id"] == 1
    assert bp_data["bp_name"] == "BP1"
    assert bp_data["bpt_id"] == 1
    assert bp_data["payment_term_id"] == 1
    assert bp_data["ten99"] == True
    assert bp_data["fedralid"] == "232464"
    assert bp_data["bp_ud_print"] == "string"
    assert bp_data["contact_person"] == "string"
    
#to create a business partner address
bp_address_payload = {
  "bp_id": 1,
  "address_id": 2,
  "default": True
}

def test_create_bp_address():
    response = requests.post("http://127.0.0.1:8000/v1/business_partner_address_associations", params={"user_token": user_token},
                             data=json.dumps(bp_address_payload)
    )
    assert response.status_code == 200
     
    bp_address_data = response.json()
    assert bp_address_data["bp_id"] == 1
    assert bp_address_data["address_id"] == 2
    assert bp_address_data["default"] == True
                             