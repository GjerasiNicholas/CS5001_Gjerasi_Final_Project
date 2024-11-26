import PySimpleGUI as sg
from subprocess_functions import ffmpeg_conversion

sg.theme('Dark Blue 2')

layout = [  [sg.Text("Select Files to Concatenate")],
            [sg.LBox([], size=(100,20), key='-FILESLB-')],
            [sg.Input(visible=False, enable_events=True, key='-IN-'), sg.FilesBrowse()],
            [sg.Button('Run'), sg.Button('Exit')]  ]

window = sg.Window('Audiobook Creator', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
      
    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))
   
    if event =="Run":
        ffmpeg_conversion(values['-IN-'].split(';'),"Overstory")

window.close()
