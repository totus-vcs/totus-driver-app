import requests

ROOT_ADDRESS = "http://10.0.0.202:5000"

def get_accellerator_pedal(): 
    # TODO: return value of position of accellerator pedal
    pass
    
def get_brake_pedal(): 
    # TODO: return value of position of brake pedal
    pass
    
def get_steering_location(): 
    # TODO: return value of position of steering wheel location
    pass

def send_to_api(address: str): 
    
    api_url = ROOT_ADDRESS + address
    print(api_url)
    
    data = { "value": 0.2 }
    
    response = requests.put(api_url, json=data)
    
    
send_to_api("/accellerator/controller_location")

