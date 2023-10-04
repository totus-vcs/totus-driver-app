import sys
import pygame
from pygame.locals import *
import requests
from time import sleep

ROOT_ADDRESS = "http://10.0.0.202:5000"
ROUND_VALUE = 1

def send_to_api(address: str, value: bool): 
    api_url = ROOT_ADDRESS + address
    print("Sending:", value, "TO:", api_url)
    data = { "value": value }
    response = requests.put(api_url, json=data)
    sleep(0.01)
    return None
 
### Initialize ###

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
motion = [0, 0]

i = 0;
brake = 0.0
accellerator = 0.0
steering = 0.0

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
                            send_to_api("/brake/controller_location", value_to_send)
                            accellerator = value_to_send
                        
                        
                    if event.value < 0:
                        
                        ### ACCELLERATOR ###
                        # print("accel", event.value)
                        value_to_send = event.value
                        value_to_send = round(value_to_send, ROUND_VALUE)
                        value_to_send = -1 * value_to_send
                        print('accellerator value: ' , value_to_send)
                        if value_to_send != accellerator: 
                            send_to_api("/accellerator/controller_location", value_to_send)
                            accellerator = value_to_send
                        
                        
                if event.axis == 0:
                    
                    ### STEERING ###
                    value_to_send = event.value
                    value_to_send = round(value_to_send, ROUND_VALUE)
                    value_to_send = value_to_send
                    print('steering value: ' , value_to_send)
                    if value_to_send != accellerator: 
                        send_to_api("/steering/controller_location", value_to_send)
                        accellerator = value_to_send
            
                            
        # # DISCONNECT ETC
        # if event.type == JOYDEVICEADDED:
        #     joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        #     for joystick in joysticks:
        #         print(joystick.get_name())
        # if event.type == JOYDEVICEREMOVED:
        #     joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        # if event.type == QUIT:
        #     pygame.quit()
        #     sys.exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_ESCAPE:
        #         pygame.quit()
        #         sys.exit()
    # clock.tick(60)