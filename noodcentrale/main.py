import tkinter as tk
from controllers.controller import NoodcentraleController
from views.view import NoodcentraleView
#REVIEW 1: database naam in main programma in een constante steken + hier initialiseren niet in db_model
#REVIEW 2: code aanpassen aan de gewijzigde controller attributen
if __name__ == "__main__":
    root = tk.Tk()
    # Maak controller zonder view
    controller = NoodcentraleController(None)
    # Maak view met controller
    view = NoodcentraleView(root, controller)
    # Koppel view aan controller
    controller.view = view
    root.mainloop()