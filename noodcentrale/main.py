import tkinter as tk
from controllers.controller import NoodcentraleController
from views.view import NoodcentraleView
from models.db_model import NoodcentraleDB

if __name__ == "__main__":
    DBNAME = "noodcentrale.db"  # REVIEW 1: constante hier in main
    db = NoodcentraleDB(DBNAME)

    root = tk.Tk()

    # Maak de hoofdcontroller aan met model
    controller = NoodcentraleController(db)

    # Maak de view aan en koppel aan controller
    view = NoodcentraleView(root, controller)
    controller.set_view(view)

    root.mainloop()
