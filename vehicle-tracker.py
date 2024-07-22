import os
import platform 
import tkinter as tk
import random
from tkinter import ttk
from tkinter import messagebox

vehicle_list = []

def add_vehicle(): 
    global vehicle_list
    print("What is the Year, Make and Model of the vehicle?")
    v_year = input("Year:")
    v_make = input("Make:")
    v_model = input("model:")
    v_ID = str(random.randint(0,1000))
    
    vehicle = v_ID + " " + v_year + " " + v_make + " " + v_model
    vehicle_list.append(vehicle)
    
    print(f"Vehicle ID: {vehicle} has been added to the list, with vehicle ID {v_ID} ")
    print(vehicle_list)

def remove_vehicle():
    global vehicle_list
    removal = input("Do you know the ID for the Vehicle to remove?")
    if removal == "no":
            print(vehicle_list)
            removal = input("Input Id for vehicle:")
    else:
        vehicle_list.remove(removal)

remove_vehicle()