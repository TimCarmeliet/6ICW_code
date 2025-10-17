import tkinter as tk

class NoodcentraleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Noodcentrale")

        # Venster automatisch aanpassen aan schermgrootte
        scherm_breedte = self.root.winfo_screenwidth()
        scherm_hoogte = self.root.winfo_screenheight()
        self.root.geometry(f"{scherm_breedte}x{scherm_hoogte}")

        self.add_gebruiker_knop = tk.Button(self.root, text="Voeg gebruiker toe")
        self.add_gebruiker_knop.grid()

        self.add_scenario_knop = tk.Button(self.root, text="Voeg scenario toe")
        self.add_scenario_knop.grid()
        

# Main programma
if __name__ == "__main__":
    root = tk.Tk()
    app = NoodcentraleGUI(root)

    #afmetingen van root printen
    root.update_idletasks()  # Zorg dat de geometry up-to-date is
    print(f"Venster breedte: {root.winfo_width()}, hoogte: {root.winfo_height()}")

    root.mainloop()