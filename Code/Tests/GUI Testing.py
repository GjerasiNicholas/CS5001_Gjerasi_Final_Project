import PySimpleGUI as sg

layout = [
    [sg.Text("Odd Even Testing", size=(50, 1))],
    [sg.Text("Put a number here"), sg.InputText()],
    [sg.Button("Odd or Even?")],
    [sg.Button("Exit")]
]

# Create the Window

window = sg.Window("Main Codebase", layout)

# create event loop

while True:
    event, values = window.read()
    # end program if user closes window or rpesses the OK button
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Odd or Even?":
        try:
            sg.popup_yes_no("Can you even see me?")
        except ValueError:
            sg.popup("Please enter a valid Integer!")
window.close()
