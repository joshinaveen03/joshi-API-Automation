import json

def payload_create_booking():
    payload = {
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
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload

def payload_create_booking_tc2():
    payload = {
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
    return payload