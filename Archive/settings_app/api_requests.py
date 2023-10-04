import requests
from time import sleep

ROOT_ADDRESS = "http://10.0.0.202:5000"

def general_message(address: str, data): 
    api_url = ROOT_ADDRESS + address
    print("Sending:", data, "TO:", api_url)
    response = requests.put(api_url, json=data)
    return response

def value_message(address: str, value): 
    api_url = ROOT_ADDRESS + address
    print("Sending:", value, "TO:", api_url)
    data = { "value": value }
    response = requests.put(api_url, json=data)
    sleep(0.01)
    return None