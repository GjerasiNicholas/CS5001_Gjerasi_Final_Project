'''
This script create a GUI which allows the user to select audio files and concatenate them based on the order in which they were selected. 
The user will be able to enter a title for the audiobook and that will be the output name of the final file. The finalized file will be
stored in the /Output/ directory within the folder structure of the workspace.

Dependencies:
    -ffmpeg (set as PATH variable)
    -PySimpleGUI (key required, this is free. See README)

Usage:
Run this script to open the GUI. Enter a name for your finalized audiobook, select the audio files from anywhere on your computer, and click "run".
'''


import PySimpleGUI as sg
from subprocess_functions import ffmpeg_conversion

sg.theme('DarkGreen7')

layout = [[sg.Text("Select Files to Concatenate (Acceptable types: mp3, m4a, m4b, aac)")],
          [sg.Text("Enter Book Name:"), sg.Input(
              key="-TITLE-", size=(20, 10))],
          [sg.LBox([], size=(100, 20), key='-FILESLB-')],
          [sg.Input(visible=False, enable_events=True,
                    key='-IN-'), sg.FilesBrowse()],
          [sg.Button('Run'), sg.Button('Exit')]
          ]

window = sg.Window('Audiobook Creator', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == '-IN-':
        window['-FILESLB-'].Update(values['-IN-'].split(';'))

    if event == "Run":

        ffmpeg_conversion(values['-IN-'].split(';'), values['-TITLE-'])

window.close()
