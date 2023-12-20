import pytest
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_http_status_code
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers_json

class TestCreateBooking(object):


    @pytest.mark.positive
    def test_create_booking_tc1(self):
        payload=payload_create_booking()
        print(payload)

        response=post_requests(url=APIConstants.url_create_booking(),
                               auth=None,
                               headers=common_headers_json(),
                               payload=payload,in_json=False)
        print(response)


        bookingid=response.json()["bookingid"]
        print(bookingid)

        verify_http_status_code(response,200)

    @pytest.mark.Negative
    def test_create_booking_tc2(self):
        response=post_requests(url=APIConstants.url_create_booking(),
                               auth=None,
                               headers=common_headers_json(),
                               payload=payload_create_booking(),in_json=False)
        verify_http_status_code(response,200)

    @pytest.mark.Negative
    def test_create_booking_tc3(self):
        response=post_requests(url=APIConstants.url_create_booking(),
                               auth=None,
                               headers=common_headers_json(),
                               payload=payload_create_booking(),in_json=False)
        verify_http_status_code(response,200)