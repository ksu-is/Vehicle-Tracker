import os
import platform 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

vehicle_list = []

def add_vehicle(): 
    vehicle_list = []
    print("What is the Year, Make and Model of the vehicle?")
    v_year = input("Year:")
    v_make = input("Make:")
    v_model = input("model:")
    vehicle = v_year + " " + v_make + " " + v_model
    vehicle_list.append(vehicle)
    print(f"Vehicle: {vehicle} has been added to the list.")


add_vehicle()