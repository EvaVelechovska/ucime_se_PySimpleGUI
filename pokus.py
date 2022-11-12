import PySimpleGUI as sg

sg.theme("DarkBlue")

layout = ([sg.Text("Ahoj světe")],
          [sg.Text("Zadej text"), sg.InputText(key="Input1", do_not_clear=True)],
          [sg.Text("Zadej další text"), sg.InputText(key="Input2", do_not_clear=True)],
          [sg.Button("Další záznam"), sg.Push(), sg.Button("OK"), sg.Button("Cancel")])

window = sg.Window("Pozdrav", layout, finalize=True)
window["Input1"].bind("<Return>", "_Enter")
window["Input2"].bind("<Return>", "_Enter")


while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    elif event == "Input1" + "_Enter":
        print(event)
    elif event == "Input2" + "_Enter":
        print(event)
    elif event == "Další záznam":
        print(values)
        window["Input1"].Update("")
        window["Input2"].Update("")
    elif event == "OK":
        print(values)

window.close()
