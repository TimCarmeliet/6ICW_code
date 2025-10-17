import tkinter as tk
from tkinter import ttk
from tkinter import font

class NoodcentraleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Noodcentrale")

        scherm_breedte = self.root.winfo_screenwidth()
        scherm_hoogte = self.root.winfo_screenheight()
        self.root.geometry(f"{scherm_breedte}x{scherm_hoogte}")

        self.root.configure(bg="#1e1e2f")

        # Dynamische fontgrootte voor knoppen (iets kleiner)
        self.knop_font = font.Font(family="Segoe UI", size=12)

        # Configureer grid van root zodat alles schaalt
        self.root.grid_rowconfigure(0, weight=1)   # Titel
        self.root.grid_rowconfigure(1, weight=2)   # Knoppen
        self.root.grid_rowconfigure(2, weight=1)   # Footer
        self.root.grid_columnconfigure(0, weight=1)

        # Hoofdtitel
        self.titel = tk.Label(
            self.root, 
            text="🚨 Noodcentrale", 
            font=("Segoe UI", 32, "bold"), 
            fg="white", 
            bg="#1e1e2f"
        )
        self.titel.grid(row=0, column=0, sticky="nsew", pady=20)

        # Frame voor knoppen
        knop_frame = tk.Frame(self.root, bg="#1e1e2f")
        knop_frame.grid(row=1, column=0, sticky="nsew")
        knop_frame.grid_columnconfigure(0, weight=1)
        knop_frame.grid_columnconfigure(1, weight=1)

        # Knoppen met dynamische tekst
        self.gebruiker_tekst = "➕ Voeg gebruiker toe"
        self.scenario_tekst = "🧩 Voeg scenario toe"

        self.add_gebruiker_knop = ttk.Button(knop_frame, text=self.gebruiker_tekst, width=14)
        self.add_gebruiker_knop.grid(row=0, column=0, padx=30, pady=20, sticky="ew", ipady=10)

        self.add_scenario_knop = ttk.Button(knop_frame, text=self.scenario_tekst, width=14)
        self.add_scenario_knop.grid(row=0, column=1, padx=30, pady=20, sticky="ew", ipady=10)

        # Stijl voor knoppen met dynamisch font
        stijl = ttk.Style()
        stijl.configure("Knop.TButton", font=self.knop_font, padding=6)
        stijl.map("Knop.TButton", background=[("active", "#3e3e5e")])
        self.add_gebruiker_knop.configure(style="Knop.TButton")
        self.add_scenario_knop.configure(style="Knop.TButton")

        # Footer
        self.footer = tk.Label(
            self.root, 
            text="© 2025 Noodcentrale Systeem 6ICW", 
            font=("Segoe UI", 10), 
            fg="#cccccc", 
            bg="#1e1e2f"
        )
        self.footer.grid(row=2, column=0, sticky="sew", pady=10)

        # Bind resize event
        self.root.bind("<Configure>", self.resize_fonts)

    def resize_fonts(self, event):
        # Dynamische fontgrootte op basis van vensterhoogte (iets kleiner)
        nieuwe_grootte = max(10, int(self.root.winfo_height() * 0.018))
        self.knop_font.configure(size=nieuwe_grootte)
        self.titel.configure(font=("Segoe UI", max(24, int(self.root.winfo_height() * 0.05)), "bold"))
        self.footer.configure(font=("Segoe UI", max(8, int(self.root.winfo_height() * 0.012))))

        # Dynamisch tekst aanpassen: als knop te smal is, splits tekst over 2 regels
        knop_frame = self.add_gebruiker_knop.master
        gebruiker_breedte = knop_frame.winfo_width() // 2
        scenario_breedte = knop_frame.winfo_width() // 2

        # Stel een drempel in voor breedte waarop tekst wordt gesplitst
        drempelwaarde = 300
        if gebruiker_breedte < drempelwaarde:
            self.add_gebruiker_knop.config(text="➕\nVoeg \ngebruiker \ntoe")
        else:
            self.add_gebruiker_knop.config(text=self.gebruiker_tekst)

        if scenario_breedte < drempelwaarde:
            self.add_scenario_knop.config(text="🧩\nVoeg \nscenario \ntoe")
        else:
            self.add_scenario_knop.config(text=self.scenario_tekst)

# Main programma
if __name__ == "__main__":
    root = tk.Tk()
    app = NoodcentraleGUI(root)
    root.mainloop()