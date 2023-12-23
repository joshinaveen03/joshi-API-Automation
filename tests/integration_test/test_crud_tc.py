from src.constants.api_constants import APIConstants
import requests

def test_case():
    #print(Base_URL)

    #url_direc_func=base_url()
    #print(url_direc_func)

    url_class=APIConstants.base_url()
    print(url_class)

    url_class1=APIConstants.url_create_booking()
    print(url_class1)

