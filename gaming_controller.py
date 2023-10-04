import pygame
from pygame.locals import *
import requests
from time import sleep

def send_to_api(ROOT_ADDRESS, address: str, value: bool): 
    api_url = "http://" + ROOT_ADDRESS + address
    print("Sending:", value, "TO:", api_url)
    data = { "value": value }
    response = requests.put(api_url, json=data)
    sleep(0.01)
    return None

def run_gaming_controller(ROOT_ADDRESS, ROUND_VALUE): 
    ### Initialize ###

    pygame.init()
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        print(joystick.get_name())

    motion = [0, 0]

    accellerator = 0.0

    ## For Every Update on Gaming Controller ##

    while True:

        # Motion holds the values from the pedals
        # It has the shape [Steering Wheel (-1,1), Pedals (-1,1)]
        # Steering Wheel: -1 is left 1 is right
        # Pedal: negative is accelerator, positive is break
        if abs(motion[0]) < 0.1:
            motion[0] = 0
        if abs(motion[1]) < 0.1:
            motion[1] = 0

        for event in pygame.event.get():
            
            if event.type == pygame.JOYAXISMOTION:
                # print(event)
                
                if event.axis < 2:
                    # gives value from -1 to 1 of motion
                    motion[event.axis] = event.value
                    if event.axis == 1:
                        if event.value > 0:
                            
                            ###  BRAKE ###
                            print("brake", event.value)
                            value_to_send = event.value
                            value_to_send = round(value_to_send, ROUND_VALUE)
                            print('brake value: ' , value_to_send)
                            if value_to_send != accellerator: 
                                send_to_api(ROOT_ADDRESS, "/brake/controller_location", value_to_send)
                                accellerator = value_to_send
                            
                            
                        if event.value < 0:
                            
                            ### ACCELLERATOR ###
                            # print("accel", event.value)
                            value_to_send = event.value
                            value_to_send = round(value_to_send, ROUND_VALUE)
                            value_to_send = -1 * value_to_send
                            print('accellerator value: ' , value_to_send)
                            if value_to_send != accellerator: 
                                send_to_api(ROOT_ADDRESS, "/accellerator/controller_location", value_to_send)
                                accellerator = value_to_send
                            
                            
                    if event.axis == 0:
                        
                        ### STEERING ###
                        value_to_send = event.value
                        value_to_send = (value_to_send + 1) /2
                        value_to_send = round(value_to_send, ROUND_VALUE)
                        print('steering value: ' , value_to_send)
                        if value_to_send != accellerator: 
                            send_to_api(ROOT_ADDRESS, "/steering/controller_location", value_to_send)
                            accellerator = value_to_send
                