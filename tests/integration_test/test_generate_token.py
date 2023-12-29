from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_token,payload_create_booking
from src.helpers.utils import common_headers_json,common_headers_for_put_delete_patch
from src.helpers.api_requests_wrapper import post_requests,put_requests

def test_create_token():
    response=post_requests(url=APIConstants.url_create_token(),
                           payload=payload_create_token(),
                           headers=common_headers_json(),
                           auth=None,
                           in_json=False)
    print(response)

    token=response.json()["token"]
    print(token)



