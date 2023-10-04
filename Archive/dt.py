import sys
import pygame
from pygame.locals import *
import requests
from time import sleep

ROOT_ADDRESS = "http://10.0.0.202:5000"

def send_to_api(address: str, value: bool): 
    api_url = ROOT_ADDRESS + address
    print("Sending:", value, "TO:", api_url)
    data = { "value": value }
    response = requests.put(api_url, json=data)
    sleep(0.01)

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)
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

while True:

    #  SCREEN STUFF
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, colors[my_square_color], my_square)
    #Work HERE
    # Motion holds the values from the pedals, it has the shape [Steering Wheel (-1,1), Pedals (-1,1)]
    #steering Wheel -1 is left 1 is right
    #pedal negative is accelerator, positive is break
    if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0
    # Stop Here
    #can remove this, just for visual on the gamescreen
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10


    for event in pygame.event.get():
        
        if event.type == pygame.JOYAXISMOTION:
            #print(event)
            if event.axis < 2:
                #gives value from -1 to 1 of motion
                motion[event.axis] = event.value
                if event.axis == 1:
                    if event.value > 0:
                        
                        #  BRAKE
                        print("brake", event.value)
                        
                        
                    if event.value < 0:
                        
                        # ACCEL
                        print("accel", event.value)
                        send_to_api("/accellerator/controller_location", event.value)
                        
                        
                if event.axis == 0:
                    
                    # STEERING
                    print("steering", event.value)
                    
                    
        # DISCONNECT ETC
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_ESCAPE:
        #         pygame.quit()
        #         sys.exit()
        

    pygame.display.update()
    # clock.tick(60)