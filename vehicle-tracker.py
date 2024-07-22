import os
import platform 
import tkinter as tk
import random
from functools import partial
from itertools import ifilter
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
    global vehicle_list2
    
    removal = input("Do you know the ID for the Vehicle to remove? ")
    if removal == "no":
            print(vehicle_list)
            removal = input("Input Id for vehicle:")
    else:
        Id_search = [word for word in vehicle_list if word in removal]
        print(Id_search)
        vehicle_list.remove(new_ID)
    

    print(vehicle_list)


def print_inventory():
     global vehicle_list
     print(vehicle_list)

def opening_menu():
     print("Welcome to J&J Car Tracker! What would you like to do?")
     menu = {}
     menu ['1'] = "Add Vehicle"
     menu ['2'] = "Remove Vehicle"
     menu ['3'] = "Find Vehicle ID"
     menu ['4'] = "Exit"
     while True: 
        options=menu.keys()
        for entry in options: 
             print (entry, menu[entry])

        selection = input("Please Select:") 
        if selection =='1': 
            add_vehicle() 
        elif selection == '2': 
            remove_vehicle()
        elif selection == '3':
            print_inventory()
        elif selection == '4': 
            break
        else: 
            print ("Unknown Option Selected!")

opening_menu()