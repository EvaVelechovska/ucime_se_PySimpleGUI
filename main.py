import PySimpleGUI as sg


sg.theme("Darkblue")

layout = ([sg.Text("Vítá Vás Label Maker",text_color="", font=("", 16), justification="Center")],
          [sg.Text("")],
          [sg.Push(), sg.Text("Jak chcete zadat štítky? ", font=(", 14")), sg.Push()],
          [sg.Push(), sg.Button("zadat ručně"), sg.Push()],
          [sg.Push(), sg.FileBrowse("Načíst ze soboru"), sg.Push()],
          [sg.Text("")],
          [sg.Button("Zavřít"), sg.Push(),sg.Button("Cancel")])

window = sg.Window("Label maker", layout, size=(300, 250))
while True:
    event, values = window.read()
    if event == "Cancel" or event == "Zavřít" or event == sg.WIN_CLOSED:
        break
    elif event == "zadat ručně":
        forma_choises = ["gtt", "sir", "sol"]
        jednotka_choises = ["ml", "mg", "pcs"]
        sg.theme("Darkblue")
        layout = [[sg.Text("Název: ", size=(15, 1)), sg.InputText()],
                  [sg.Text("množství: ", size=(15, 1)), sg.InputText()],
                  [sg.Text("jednotka: ", size=(15, 1)), sg.OptionMenu(jednotka_choises)],
                  [sg.Text("forma: ", size=(15, 1)), sg.OptionMenu(forma_choises)],
                  [sg.Text("cena: ", size=(15, 1)), sg.InputText()],

                  [sg.Button("Ulož"), sg.Button("Další záznam"), sg.Push(), sg.Button("Cancel")]]

        window = sg.Window("Zadejte", layout)
        while True:
            event, values = window.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                break
            elif event == "Ulož":
                #  TODO export?
                print("zadáno", values)
            elif event == "Další záznam":
                # uložý co je napsáno a vyprázdní okýnka
                #  TODO najít způsob, jak vyprázdnit chlívečky
                print("další záznam")

        window.close()

    elif event == "Načíst ze souboru":
        print("načteno a vyrobeno")

window.close()

