import os
import platform 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

vehicle_list = []

def add_vehicle(): 
    print("What is the Year, Make and Model of the vehicle?")
    v_year = input("Year:")
    v_make = input("Make:")
    v_model = input("model:")
    vehicle = v_year + v_make + v_model
    vehicle_list = vehicle_list.append(vehicle)
    
