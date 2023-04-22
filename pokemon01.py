import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import ctypes
import os
import requests
from poke_api import get_Pokemon_Name_List, download_pokemon_artwork

# Define the Pastebin API endpoint and credentials
PASTEBIN_API_ENDPOINT = 'https://pastebin.com/api/api_post.php'
PASTEBIN_API_DEV_KEY = 'https://pastebin.com/api/api_post.php'
PASTEBIN_API_USER_KEY = 'ESLuNubbvmkeJWuN9MxICyprJzhY48wV'

# Define a function to upload a string to Pastebin and return the resulting URL


def upload_to_pastebin(text):
    payload = {
        'api_dev_key': PASTEBIN_API_DEV_KEY,
        'api_user_key': PASTEBIN_API_USER_KEY,
        'api_option': 'paste',
        'api_paste_code': text,
    }
    response = requests.post(PASTEBIN_API_ENDPOINT, data=payload)
    if response.status_code == 200 and response.text.startswith('https://pastebin.com/'):
        return response.text.strip()
    else:
        return None

# Define the window
window = tk.Tk()
window.title("POKEMON IMAGE VIEWER")
window.geometry("700x900")
window.resizable(True, True)

# Set the window icon
# window.iconbitmap("icon.ico")

# Define a image_Frame
image_Frame = ttk.Frame(window, padding=10,border=5)
image_Frame.grid(column=0, row=0, sticky="nsew")

# Define a Image
Image = Image.open(
    "C:\\Users\\gauta\\OneDrive\\Desktop\\poke.jpg")
Image = ImageTk.PhotoImage(Image)
label = ttk.Label(image_Frame, image=Image, justify=["center"])
label.grid(column=0, row=0, columnspan=2)

# Define a Combobox
Pokemon_Name_List = get_Pokemon_Name_List()
Selected_Pokemon = tk.StringVar()
combobox = ttk.Combobox(
    image_Frame, textvariable=Selected_Pokemon, values=Pokemon_Name_List, justify=["center"])
combobox.grid(column=0, row=1, columnspan=2)

# Define button to set the image as desktop background


def Set_Your_Walpaper():
    path = os.path.join(os.getcwd(), f"{Selected_Pokemon.get()}.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


Set_walpaper = ttk.Button(
    image_Frame, text="Set as Desktop Image", command=Set_Your_Walpaper)
Set_walpaper.grid(column=0, row=3, columnspan=2)
Set_walpaper.configure(state="disabled")

# Define event handlers


# combobox.bind("<<ComboboxSelected>>", on_combobox_selected)

# Run the GUI
window.mainloop()
