from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
from src.helpers.common_verification import verify_http_status_code
from src.helpers.payload_manager import payload_create_booking_dynamic
from src.helpers.utils import common_headers_json


class Test_create_booking(object):


    def test_createbooking_01(self):
        payload = payload_create_booking_dynamic()
        print(payload)

        response = post_requests(url=APIConstants.url_create_booking(),
                                 auth=None,
                                 headers=common_headers_json(),
                                 payload=payload, in_json=False)
        print(response)
        bookingid = response.json()["bookingid"]
        print(bookingid)

        verify_http_status_code(response, 200)

