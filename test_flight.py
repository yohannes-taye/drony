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

def arm_and_takeoff(aTargetAltitude): 
    vehicle.armed=True 
    
    while vehicle.armed==False: 
        print("Arming motor...")
        time.sleep(1)
    

    print("Taking off.. ")
    vehicle.simple_takeoff(aTargetAltitude)
    
    while True: 
        print("current altitude: %f"%vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude*.95: 
            break; 
        time.sleep(1)
    
    print("Target altitude reached")
    
    return None 

vehicle = connectMyCopter() 
print("HERE1")
vehicle.mode=VehicleMode("GUIDED")
arm_and_takeoff(5)
vehicle.mode=VehicleMode("LAND")

while True: 
    time.sleep(2)

vehicle.close() 
# arm() 
