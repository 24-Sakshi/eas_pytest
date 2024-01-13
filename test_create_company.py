import pytest
import requests
from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI
import json
app = FastAPI()
client = TestClient(app,base_url="http://127.0.0.1:8000/v1")

#openapi file path = "E:\Shubhchintak Technology Pvt Ltd\Project\EAS Project\eas_pytest\openapi.json"

user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQxNjg5NDE1ZWMyM2EzMzdlMmJiYWE1ZTNlNjhiNjZkYzk5MzY4ODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWlzZnQtZWFzLTliYmRlIiwiYXVkIjoiYWlzZnQtZWFzLTliYmRlIiwiYXV0aF90aW1lIjoxNzA1MTM3ODA0LCJ1c2VyX2lkIjoiSk1Vekg3dE1keFE4MG40Y3lJcVJmZTVzemd1MSIsInN1YiI6IkpNVXpIN3RNZHhRODBuNGN5SXFSZmU1c3pndTEiLCJpYXQiOjE3MDUxMzc4MDQsImV4cCI6MTcwNTE0MTQwNCwiZW1haWwiOiJkZWVwYWxpbmdoYWRpYTE2MDZAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImRlZXBhbGluZ2hhZGlhMTYwNkBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.BDuW1z0Fcdu90P80GurLxhfESnhnZ_aqDNPKt6uPEUO6vsb29JxPNOxDLwMZcPMaGYw_tg9HZm2lDbMNeqwRet6pyDZB_JjYrYmEN4E-8p87KCUdC0HclTxYH9PINSNtFXs5G8-8WgfMJBKDt19smmoZy63blBbbhzqwdpwN9Gtwr1n32MgtBJgxMyZPy0vN_yiQ5gcTnqvp9KVXI0o5OoGfzvmqqOaQU-u7p7PPVpniG7MZSfIj9gfaWYyp-ImyXI-RUdfnCw0C1LMltl8O30gzX8whFJe4pQWOjhddEVME1K06FyHCVJLQxBtoISn__Wrih-PwyHSiBzdm1xiSIQ" 

payload = {
            "company_name": "XYZABC",
            "fedral_id": "341876786",
            "doi": "2024-01-12",
            "bpic_id": 2,
            "company_type_id": 2,
            "industry_id": 2,
            "company_plan": 0,
            "inventory": True,
            "sales_tax_percentage": 5,
            "tax_behavior": True,
            "year_beginning": "2024-01-12",
            "is_cash": True,
            "is_inventory": True
        }

# base_url="http://127.0.0.1:8000/v1"
def test_create_company():
    # Use your API to create a company
    response = requests.post("http://127.0.0.1:8000/v1/companies/create",params={"user_token": user_token},
        data=json.dumps(payload)
    )
    
    print("\n\n",response.text,"\n\n")
    # Check the response status code
    assert response.status_code == 200

    # Check the response JSON data
    company_data = response.json()
    assert company_data["company_name"] == "XYZABC"