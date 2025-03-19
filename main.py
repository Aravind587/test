import eel

eel.init('Gui')

@eel.expose
def App():
    print("Application is running")

App()
eel.start('file.html',size=(500,500))
