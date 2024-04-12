import pytest
import allure
from src.constants.apiconstants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import verify_http_status_code,verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("verify that create booking status and booking id shouldnt be null")
    @allure.description("create a booking from payload and verify that the booking id shdnt be null and statuscode is 200 fr crrct payload")
    def test_create_booking_positive(self):
        #url, payload and headers
        response = post_request(url=APIConstants.url_create_booking(),
                        auth=None,
                        headers=Util().common_headers_json(),
                        payload=payload_create_booking(),
                        in_json=False)
        booking_id = response.json()["bookingid"]

        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)




