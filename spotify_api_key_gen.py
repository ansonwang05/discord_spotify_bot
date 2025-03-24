from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    '''
    Using Client Credentials Flow to get an access token
    
    Args:
        Valid CLIENT ID and CLIENT SECRET

    Returns:
        Spotify Access Token that will last for 1 hour
    '''
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64 ,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_json_data():
    '''
    Using Client Credentials Flow to get an access token
    to get a spotify access token that will only last 1 hour
    Will need a valid CLIENT ID and valid CLIENT SECRET
    
    Args:
        None

    Returns:
        None
    '''
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64 ,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    return json_result

def print_json_data(json_result): 
    '''
    Prints the results of the json file returned by
    get_json_data() in a readable manner

    Args:
        json_result (json object): a valid json object

    Returns:
        None
    '''
    access_token = json_result["access_token"]
    token_type = json_result["token_type"]
    expires_in = json_result["expires_in"]
    print(f"access_token: {access_token}\ntoken_type: {token_type}\nexpires_in: {expires_in}\n")

def get_json_specific(json_result, key):
    '''
    Uses a json object and a specfic key value in the json object
    to return the value of that key

    Args:
        json_result (json object) : a valid json object 
        key (string of key) : a valid key in the json object

    Returns: 
        The value of the key in the json_result
    '''
    match key:
        case "access_token":
            return json_result["access_token"]
        case "token_type":
            return json_result["token_type"]
        case "expires_in":
            return json_result["expires_in"]
        case _:
            return "Please enter a correct key value"

# json_object = get_json_data()
# print_json_data(json_object)
# access_token = get_json_specific(json_object, "access_token")
# token_type = get_json_specific(json_object, "token_type")
# expires_in = get_json_specific(json_object, "expires_in") 
# print(f"access_token: {access_token}\ntoken_type: {token_type}\nexpires_in: {expires_in}\n")
