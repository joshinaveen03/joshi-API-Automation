import json
from faker import Faker

faker=Faker()

def payload_create_booking():
    json_payload = {
        "firstname": "Joshi",
        "lastname": "Allen",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "midnight snack"
    }
    return json_payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast","parking""midnight snack"))
    }
    return payload
