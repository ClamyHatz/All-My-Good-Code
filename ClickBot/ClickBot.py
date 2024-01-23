import tkinter as tk
from pyautogui import *
import pyautogui
import time
import threading
import win32api, win32con

def click():
    global click_count
    click_count = click_count + 1
    label.config(text="Click Count: " + str(click_count))
    print("clicked!")
    win32api.SetCursorPos((600, 690))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    root.update()

def toggle():
    global running
    global stopper
    running = True
    stopper = False
    if running:
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL, fg ="red")
        runs.config(text="Running", fg="green")
        root.update()
        start_player_thread()
    else:
        start_button.config(text="Start")

def start_player_thread():
    global player_thread
    player_thread = threading.Thread(target=player)
    player_thread.start()

def off():
    root.destroy()

def player():
    global running
    global click_count
    root.update()
    while running and not stopper and click_count <= 24:
        runs.config(text="Waiting", fg="red")
        time.sleep(5)
        global found
        found = False
        while not found:
            runs.config(text="Searching...", fg="Blue")            
            pic = pyautogui.screenshot(region=(590, 590, 100, 100))
            width, height = pic.size
            for x in range(0, width, 1):
                for y in range(0, height, 1):
                    r, g, b = pic.getpixel((x, y))

                #RGB range for green color
                if r in range(216, 236) and g in range(222, 242) and b in range(105, 125):
                    click()
                    time.sleep(0.05)
                    found = True
                    break
                else:
                    print("Not Found!")
                    time.sleep(5)
                    break
             
    if click_count >= 24:
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED, fg ="black")
        runs.config(text="Complete!", fg="green")
        click_count = 0

# Create the main window
root = tk.Tk()
root.geometry("200x150")
root.resizable(False, False)

# Variable to track whether the player is running
running = False
stopper = True
found = False

# Click counter
global click_count
click_count = 0

# Runs label
runs = tk.Label(root, text="Not Running", fg="grey")
runs.grid(row=0, column=1, columnspan=2, pady=10)

# Start button
start_button = tk.Button(root, text="Start", command=toggle)
start_button.grid(row=1, column=1, padx=5, pady=5)

# Stop button
stop_button = tk.Button(root, text="KILL", command=off, state=tk.DISABLED)
stop_button.grid(row=1, column=2, padx=5, pady=5)

# Click count label
label = tk.Label(root, text="Click Count: " + str(click_count))
label.grid(row=3, column=1, columnspan=2, pady=10,)

# Center all elements
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Run the main loop
root.mainloop()