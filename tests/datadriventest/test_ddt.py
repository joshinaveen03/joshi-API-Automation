# Read the CSV pr Excel file
# Create a function create_token which can take values from the excel file
# verify the Expected result

# Read the excel file - openpyxl
import openpyxl
import requests
import pytest
import allure
import allure_pytest

from src.constants.api_constants import APIConstants
#from src.helpers.api_requests_wrapper import post_requests
#from src.helpers.payload_manager import payload_create_token
from src.helpers.utils import common_headers_json


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(APIConstants.url_create_token(),
                             headers=common_headers_json(),
                             )
    return response


def test_post_create_token():
    file_path = "tests/datadriventest/testdata_ddt.xlsx"

    credentials = read_credentials_from_excel(file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)

