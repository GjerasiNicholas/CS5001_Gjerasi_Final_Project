import PySimpleGUI as sg
from subprocess_functions import ffmpeg_conversion

sg.theme('Dark Blue 2')

layout = [  [sg.Text("Select Files to Concatenate (Acceptable types: mp3, m4a, m4b, aac)")],
            [sg.Text("Enter Book Name:"),sg.Input(key ="-TITLE-",size=(20,10))],
            [sg.LBox([], size=(100,20), key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Run'), sg.Button('Exit')]  
        ]

window = sg.Window('Audiobook Creator', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
      
    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))
   
    if event =="Run":

        ffmpeg_conversion(values['-IN-'].split(';'), values['-TITLE-'])

window.close()
