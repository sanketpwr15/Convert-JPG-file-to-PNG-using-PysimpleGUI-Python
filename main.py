import PySimpleGUI as sg
from PIL import Image
from pillow_heif import register_heif_opener
import os

sg.theme('DarkBlue')   # windoews theam 

# All the stuff inside your window.
layout = [  [sg.Text('Image converter', enable_events=True,
                        key='-TEXT-', font=('Arial bold', 15),
                        expand_x=True, justification='center') ,
                        sg.T("")], [sg.Text("Choose a file: "), sg.Input(size=(50, 1),key="-IN-"),#browse button
                        sg.FileBrowse(file_types=[("jpg files","*.jpg" )]),sg.T("")],[sg.T("")],#browse file 
                        [sg.Button('Convert'), sg.Button('Cancel')] #buttons
         ]

# Create the Window
window = sg.Window('Image converter', layout,size=(550,150))

# Event Loop to process "events" and button functions
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Convert':#convert button clicked
        heic_files = values["-IN-"]
        temp_img = Image.open(heic_files)
        png_photo = heic_files.replace('.jpg','.png')
        temp_img.save(png_photo)

window.close()