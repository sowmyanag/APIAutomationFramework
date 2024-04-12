#API Constants -  Class which contain all the endpoints
#keep all the urls
#static method - which can be called by , without creating a object ie., directly usiny class

class APIConstants(object):

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

#update - put, patch, delete, booking_id

    def url_put_patch_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)