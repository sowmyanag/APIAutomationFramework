def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code ==  expect_data,"failed ER! = AR"

def verify_json_key_for_not_null(key):
    assert key != 0, "key is non empty" +key
     