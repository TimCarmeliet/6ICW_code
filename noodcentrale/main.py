import tkinter as tk
from controllers.controller import NoodcentraleController
from views.view import NoodcentraleView

if __name__ == "__main__":
    root = tk.Tk()
    # Maak controller zonder view
    controller = NoodcentraleController(None)
    # Maak view met controller
    view = NoodcentraleView(root, controller)
    # Koppel view aan controller
    controller.view = view
    root.mainloop()