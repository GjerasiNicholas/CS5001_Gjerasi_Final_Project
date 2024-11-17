import PySimpleGUI as sg

layout = [
    [sg.Text("Odd Even Testing",size = (50,1))],
    [sg.Text("Put a number here"), sg.InputText()],
    [sg.Button("Odd or Even?")],
    [sg.Button("Exit")]
]

#Create the Window

window = sg.Window("Main Codebase",layout)

#create event loop

while True:
        event, values = window.read()
        #end program if user closes window or rpesses the OK button
        if event == sg.WIN_CLOSED or event =="Exit":
                break
        elif event == "Odd or Even?":
                try:
                        number = int(values[0])
                        if number % 2 == 0:
                                sg.popup("You entered an even number!")
                        elif number % 2 == 1:
                                sg.popup("You entered an odd number!")
                except ValueError:
                        sg.popup("Please enter a valid Integer!")
window.close()