from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException 
import time 
import socket 
import math 
import argparse 


def connectMyCopter(): 
    print("Connecting...") 
    baud_rate = 57600 
    vehicle = connect("/dev/ttyAMA0", baud=baud_rate, wait_ready=True)
    return vehicle

def arm(): 
    print(vehicle.mode)
    # while vehicle.is_armable==False: 
    #     print("Wating for drone to be armable!")
    #     time.sleep(1)

    print("Arming drone... ")

    vehicle.armed=True 
    while vehicle.armed==False: 
        print("Wating for the drone to be armed!")
        time.sleep(1)
    
    print("ARMED")   
    return None 

vehicle = connectMyCopter() 
arm() 
