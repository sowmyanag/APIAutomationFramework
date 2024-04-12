# Create token
#create booking id
#update the booking -- boooking ID, token
#delete the booking

#verify that created booking ID when we update , is it getting updated and delete it

import pytest
import allure
from src.constants.apiconstants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


def put_requests():
    pass


def verify_json_key_for_not_null_token(param):
    pass


class TestCrudBooking(object):
    @pytest.fixture()
    def create_token(self):
        response = post_request(
            url= APIConstants.url_create_token(),
            headers= Util().common_headers_json(),
            auth=None,
            payload=payload_create_token(),
            in_json=False
        )
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])
        return response.json()["token"]


    @pytest.fixture()
    def get_booking_id(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        booking_id = response.json()["bookingid"]

        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    def test_update_booking_id_token(self,create_token,get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_put_patch_delete(booking_id=booking_id)
        response = put_requests(
            url= put_url,
            headers = Util.common_headers_put_patch_delete_cookie(token=token),
            payload = payload_create_booking(),
            auth = None,
            in_json = False
        )
        print(response.json())
        verify_http_status_code(response_data=response,expect_data=200)


    def test_delete_booking_id(self):
        pass



