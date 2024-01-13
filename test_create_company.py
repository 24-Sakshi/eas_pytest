import pytest
import requests
from fastapi.testclient import TestClient
from fastapi import Depends, FastAPI
import json
app = FastAPI()
client = TestClient(app,base_url="http://127.0.0.1:8000/v1")


#openapi file path = "E:\Shubhchintak Technology Pvt Ltd\Project\EAS Project\eas_pytest\openapi.json"

user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQxNjg5NDE1ZWMyM2EzMzdlMmJiYWE1ZTNlNjhiNjZkYzk5MzY4ODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWlzZnQtZWFzLTliYmRlIiwiYXVkIjoiYWlzZnQtZWFzLTliYmRlIiwiYXV0aF90aW1lIjoxNzA1MTUwMjg4LCJ1c2VyX2lkIjoibkF6UVlkTkJ5bVRDYUxkWkVXZTM1dFdBUEI4MyIsInN1YiI6Im5BelFZZE5CeW1UQ2FMZFpFV2UzNXRXQVBCODMiLCJpYXQiOjE3MDUxNTAyODgsImV4cCI6MTcwNTE1Mzg4OCwiZW1haWwiOiJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.Kx8zb3_twagkZRSytOEoSV4jMZ306owZiXb16TmL6G4WaiXOgwJfes2R71Nd4LoOeqg_JmKfTa9gI1Pgr4WaFA1Rn9ft6Aw4-eyb51zWdEa6N4j3vLFbzcsEYZ9zU9BmaRGoyeUVjvEHaK24icZamr5sgl_DFEfN7kwAY69y8S-nVl_Ie61T_3G9gek8Uoj71rYnMvXm1EBCFb2WA234YOlSU8Evw1cbPp2oLmFWV_hXtmhw6vUHxYNUrJ4HbNn-EiFDPEtEpcvEjAkmAjhAPuRh6zsqx_um0209uX_KnVVJzz20JkaC-nP3-g7Sk01yviuzO-O6ZhL2AvkPiePzkQ"
# payload = {
#             "company_name": "XYZABC",
#             "fedral_id": "341876786",
#             "doi": "2024-01-12",
#             "bpic_id": 2,
#             "company_type_id": 2,
#             "industry_id": 2,
#             "company_plan": 0,
#             "inventory": True,
#             "sales_tax_percentage": 5,
#             "tax_behavior": True,
#             "year_beginning": "2024-01-12",
#             "is_cash": True,
#             "is_inventory": True
#         }

# # base_url="http://127.0.0.1:8000/v1"
# def test_create_company():
#     # Use your API to create a company
#     response = requests.post("http://127.0.0.1:8000/v1/companies/create",params={"user_token": user_token},
#         data=json.dumps(payload)
#     )
    
#     print("\n\n",response.text,"\n\n")
#     # Check the response status code
#     assert response.status_code == 200

#     # Check the response JSON data
#     company_data = response.json()
#     assert company_data["company_name"] == "XYZABC"
    
# #after creating company check whether docu type and gl determination is created or not
# user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImQxNjg5NDE1ZWMyM2EzMzdlMmJiYWE1ZTNlNjhiNjZkYzk5MzY4ODQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vYWlzZnQtZWFzLTliYmRlIiwiYXVkIjoiYWlzZnQtZWFzLTliYmRlIiwiYXV0aF90aW1lIjoxNzA1MTM3NDgyLCJ1c2VyX2lkIjoibkF6UVlkTkJ5bVRDYUxkWkVXZTM1dFdBUEI4MyIsInN1YiI6Im5BelFZZE5CeW1UQ2FMZFpFV2UzNXRXQVBCODMiLCJpYXQiOjE3MDUxMzc0ODIsImV4cCI6MTcwNTE0MTA4MiwiZW1haWwiOiJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzYWtzaGlyYXV0Mzk4QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.M8KGGo2kkgqs2v523iBVmRpheIOgxvq4hn6w1eHfo_y7cYXibB7Ve2DK4OG-fq3ahDhsDKwfoqTKWx176dz_zBXG4eBXkdkntM1VLQxyA9fXf9dLje7niCOukhItSp4-xNe3WTe_RkBSRCizWKjWODjYq2NzM_gNXqevj8HXcON5MnpzedhHXKKmb93jvbmlu-aTvH9YMSOVS8XrYLzFWpNNc33oLUQ_ajx3XVCZZ_EJRvHPFrvN4pQOe8ZtbyKz6ZJYY6xeIMY_3tHHBrMqrpLEz9ku3-VFVwyELnBwgzsUgqIOluIis_cIZNjgKIUpL-Ji3GU5sApG0IAEQrtYVQ"

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
    response = requests.post("http://127.0.0.1:8000/v1/companies/create", params={"user_token": user_token},
        data=json.dumps(payload)
    )
    
    # Check the response status code
    assert response.status_code == 200

    # Check the response JSON data
    company_data = response.json()
    assert company_data["company_name"] == "XYZABC"

    # Create an address in the address master
    company_address = {
        "company_id": 1,
        "address_id": 1,
        "default": True
    }

    address_response = requests.post("http://127.0.0.1:8000/v1/company_address_association", params={"user_token": user_token},
        data=json.dumps(company_address)
    )

    # Check the address response status code
    assert address_response.status_code == 200

    # Check the address response JSON data
    address_data = address_response.json()
    assert address_data["company_id"] == 1
    assert address_data["address_id"] == 1
    assert address_data["default"] == True
    # assert address_data["add_line_1"] == "123 Main St"
    # assert address_data["add_line_2"] == "Apt 4B"
    # assert address_data["city"] == "New York"
    # assert address_data["zip_code"] == "10001"
    # assert address_data["email"] == "example@example.com"
    # assert address_data["phone_no"] == 1234567890
    # assert address_data["country"] == "USA"
    # assert address_data["state"] == "NY"
    # assert address_data["address_type"] == True