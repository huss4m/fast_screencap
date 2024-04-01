import getpass
import keyboard
from PIL import ImageGrab
import os
import pygetwindow as gw

user = getpass.getuser()

img_folder = f"C:\\Users\\{user}\\Downloads\\Screenshots\\"

if not os.path.exists(img_folder):
    os.makedirs(img_folder)


def file_exists(name, folder):
    index = 1
    while True:
        file_path = os.path.join(folder, f"{name}_{index}.png")
        if not os.path.exists(file_path):
            return file_path
        index += 1

def screenshot_full():
    capture = ImageGrab.grab()
    path = file_exists("Screenshot", img_folder)
    capture.save(path)
    print("Capture d'écran sauvegardée :", path)


def screenshot_active_window():
    active_window = gw.getActiveWindow()
    if active_window is None:
        print("Erreur")
        return



    capture = ImageGrab.grab(bbox=(active_window.box))
    path = file_exists("Screenshot", img_folder)
    capture.save(path)
    print("Capture d'écran sauvegardée :", path)
def keypress(event):
    if event.event_type == 'down' and event.name == 'f12' and keyboard.is_pressed('ctrl'): # CTRL+F12 for full screen capture
        screenshot_full()

    if event.name == 'f12': # F12 for active window only
        screenshot_active_window()


keyboard.on_press(keypress)

keyboard.wait('esc')