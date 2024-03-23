# -*- coding: utf-8 -*-
"""
Creates folder structure for a data science project 

Created by André Rizzo in May 11th, 2019
Updated by André Rizzo in March 23th, 2024

Version: 2.0
"""

import tkinter as tk
from tkinter import filedialog
import os

# Create a folder structure
root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory(initialdir="/")
os.chdir(file_path)
path = os.getcwd()
print("Create project structure at", path)
print("")
project_name = input("Enter the project name: ")
if not os.path.exists(project_name):
    os.mkdir(project_name)
    print("Folder", project_name.upper(), "created")
    os.chdir(project_name)
    os.mkdir("data")
    print("Folder DATA created")
    os.mkdir("data/raw")
    print("Folder data/RAW created")
    os.mkdir("data/processed")
    print("Folder data/PROCESSED created")
    os.mkdir("notebooks")
    print("Folder NOTEBOOKS created")
    os.mkdir("notebooks/r")
    print("Folder NOTEBOOKS/R created")
    os.mkdir("notebooks/python")
    os.mkdir("scripts")
    print("Folder SCRIPTS created")
    os.mkdir("scripts/r")
    print("Folder SCRIPTS/R created")
    os.mkdir("scripts/python")
    print("Folder SCRIPTS/PYTHON created")
    os.mkdir("reports")
    print("Folder SCRIPTS/REPORTS created")
    os.mkdir("reports/figures")
    print("Folder SCRIPTS/REPORTS/FIGURES created")
    os.mkdir("models")
    print("Folder MODELS created")
    os.mkdir("docs")
    print("Folder DOCS created")
    os.mkdir("env")
    print("Folder ENV created","\n")
    input("Press any key to continue ...")
else:
    print("")
    print("Folder already exists.")
    input("Press any key to continue ...")


