import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_http_status_code, verify_response_key_should_not_be_none
from src.helpers.payload_manager import payload_create_token, payload_create_booking
from src.helpers.utils import common_headers_json


@pytest.fixture(scope="session")
def create_token(self):
    response = post_requests(url=APIConstants.url_create_token(),
                             payload=payload_create_token(),
                             headers=common_headers_json(),
                             auth=None, in_json=False)
    print(response)
    verify_http_status_code(response, 200)

    token = response.json()["token"]
    print(token)

    verify_response_key_should_not_be_none(token)
    return token


@pytest.fixture(scope="session")
def create_booking(self):
    response = post_requests(
        url=APIConstants.url_create_booking(),
        auth=None,
        payload=payload_create_booking(),
        headers=common_headers_json(), in_json=False
    )
    print(response)

    bookingid = response.json()["bookingid"]
    print(bookingid)

    verify_response_key_should_not_be_none(response.json()["bookingid"])

    verify_http_status_code(response, 200)

    return bookingid
