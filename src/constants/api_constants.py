# Base_URL="https://restful-booker.herokuapp.com"

# def base_url():
# return "https://restful-booker.herokuapp.com"


class APIConstants(object):



    def base_url():
        return "https://restful-booker.herokuapp.com"




    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"




    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # Patch, Put, Delete




    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/bookingid/" + str(self, booking_id)
