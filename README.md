# TOTUS Driver App - 2023

A series of scripts to control the TOTUS veichle control system - control from the driver side. 

## Description

TOTUS is a human oriented solution for the trucking industry. It's a remote control vehicle system that empowers truck drivers to operate their vehicles from the comfort of their homes or local stations, while preserving the human element of the profession. 

This iteration of the project is a part of the ANU Capstone project. This year's focus is creating a retrofit proof of concept to a Ford Focus. 

This repository contains code for the driver side - showing outputted video stream, and ability to turn on and off the steering, accellerator and brake pedals as well as control them. 
The control works for a Logitech gaming steering wheel. 

## Getting Started

### Dependencies & Virtual Environemnt

It is recommended this code is run in a python virtual environment: 

1. Make a virtual environemnt
`python -m venv venv`

2. Start the venv
`Venv\Scripts\activate.ps1`

3. Type this command if you have errors on windows
`Set-ExecutionPolicy -Scope CurrentUser Unrestricted`

4. Install requirements in your virtual environment
`pip install -r requirements.txt`

### Components

*main.py* 
* Multithreading run of all components

*gaming_controller.py*
* Recieves input from Logitech Steering wheel
* Sends to API 

*settingsApp.py*
* easy turn off and on devices

## Authors

Evangeline Sturges
[@evieeangeline](https://github.com/evieeangeline/evieeangeline.github.io)
