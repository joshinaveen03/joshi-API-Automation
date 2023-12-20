
import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests,get_requests,put_requests
from src.helpers.common_verification import verify_http_status_code, verify_response_key_should_not_be_none
from src.helpers.payload_manager import payload_create_token, payload_create_booking
from src.helpers.utils import common_headers_json,common_headers_for_put_delete_patch


class TestCreateBooking(object):

    @pytest.fixture()
    def test_create_token(self):
        response=post_requests(
            url=APIConstants.url_create_token(),
            auth=None,
            payload=payload_create_token(),
            header=common_headers_json(),
            in_json=False
            )
        verify_http_status_code(response,200)
        token=response.json()["token"]
        print(token)

        verify_response_key_should_not_be_none(token)
        return token


    def test_create_booking(self):
        response = post_requests(
            url=APIConstants.url_create_booking(),
            auth=None,
            payload=payload_create_booking(),
            headers=common_headers_json(), in_json=False

        )
        print(response)

        bookingid = response.json()["bookingid"]
        print(bookingid)

        verify_http_status_code(response, 200)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        return bookingid

    def test_update_booking(self,create_token,create_booking):
        bookingid=create_booking

        put_url=APIConstants.url_create_booking()+"/"+str(bookingid)

        response=put_requests(url=put_url,headers=common_headers_for_put_delete_patch(),
                              auth=None,payload=payload_create_booking(),in_json=False)
        print(response)