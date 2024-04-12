#class or functions

import requests
import json

def get_request(url,auth):
    response = requests.get(url=url,auth=auth)
    return response.json()

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.put(url=url,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.patch(url=url,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response
def post_request(url,auth,headers,payload,in_json):
    post_response = requests.delete(url=url,headers=headers,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return post_response


