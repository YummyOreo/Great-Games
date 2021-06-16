import tkinter as tk
from tkinter import filedialog, Text
import os
from os import system

root = tk.Tk()
apps = []

def runMain():
	os.system("python main.py")

def runSlowmode():
	os.system("python slowmode.py")

def runSlowmode():
	os.system("python ./api/api.py")

Main = tk.Button(root, text="Run Main", padx=5, pady=5, fg="white", bg="black", command=runMain)
Main.pack()

Slowmode = tk.Button(root, text="Run Slowmode", padx=10, pady=10, fg="white", bg="black", command=runSlowmode)
Slowmode.pack()

API = tk.Button(root, text="Run API", padx=10, pady=10, fg="white", bg="black", command=runSlowmode)
API.pack()


root.mainloop()
	