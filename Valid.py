import PySimpleGUI as sg

def validate_serial(serial):
    # Implement your serial number validation logic here
    # For example, check if the serial matches a predefined pattern or is present in a database
    # Return True if valid, False otherwise
    return True

def main():
    sg.theme("DarkGrey4")  # Set the GUI theme

    # Initialize the serial number variable
    serial_number = ""

    layout = [
        [sg.Text("Enter Serial Number:")],
        [sg.InputText(key="-SERIAL-", default_text=serial_number)],  # Set the default value
        [sg.Button("Validate"), sg.Button("Exit")]
    ]

    window = sg.Window("Anti-Piracy Screen", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Validate":
            serial_number = values["-SERIAL-"]
            if validate_serial(serial_number):
                sg.popup("Serial number is valid!", title="Success")
            else:
                sg.popup("Invalid serial number. It is a serious crime to pirate video games. Please report this to the police.", title="Error")

    window.close()

if __name__ == "__main__":
    main()
