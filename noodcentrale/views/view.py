import tkinter as tk
from tkinter import ttk, font, simpledialog, messagebox
#REVIEW 1 - commentaar om opbouw leesbaarder te maken
#OPTIONEEL = getters voorzien voor de attributen + data encapsulatie afdwingen door private maken van de attributen, maar voor eerste versie zeker ok
class NoodcentraleView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Noodcentrale")
        
        scherm_breedte = self.root.winfo_screenwidth()
        scherm_hoogte = self.root.winfo_screenheight()
        self.root.geometry(f"{scherm_breedte}x{scherm_hoogte}")

        self.root.configure(bg="#1e1e2f")
        self.knop_font = font.Font(family="Segoe UI", size=12)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=2)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.titel = tk.Label(
            self.root, 
            text="🚨 Noodcentrale", 
            font=("Segoe UI", 32, "bold"), 
            fg="white", 
            bg="#1e1e2f"
        )
        self.titel.grid(row=0, column=0, sticky="nsew", pady=20)

        knop_frame = tk.Frame(self.root, bg="#1e1e2f")
        knop_frame.grid(row=1, column=0, sticky="nsew")
        knop_frame.grid_columnconfigure(0, weight=1)
        knop_frame.grid_columnconfigure(1, weight=1)

        self.gebruiker_tekst = "➕ Voeg gebruiker toe"
        self.scenario_tekst = "🧩 Voeg scenario toe"

        # Verbind knoppen aan controller-methodes
        self.add_gebruiker_knop = ttk.Button(
            knop_frame, text=self.gebruiker_tekst, width=14,
            command=self.open_gebruiker_dialog
        )
        self.add_gebruiker_knop.grid(row=0, column=0, padx=30, pady=20, sticky="ew", ipady=10)

        self.add_scenario_knop = ttk.Button(
            knop_frame, text=self.scenario_tekst, width=14,
            command=self.open_scenario_dialog
        )
        self.add_scenario_knop.grid(row=0, column=1, padx=30, pady=20, sticky="ew", ipady=10)

        stijl = ttk.Style()
        stijl.configure("Knop.TButton", font=self.knop_font, padding=6)
        stijl.map("Knop.TButton", background=[("active", "#3e3e5e")])
        self.add_gebruiker_knop.configure(style="Knop.TButton")
        self.add_scenario_knop.configure(style="Knop.TButton")

        # Toevoegen: lijst met gebruikers en scenario's
        self.lijsten_frame = tk.Frame(self.root, bg="#1e1e2f")
        self.lijsten_frame.grid(row=3, column=0, sticky="nsew", padx=30, pady=10)
        self.lijsten_frame.grid_columnconfigure(0, weight=1)
        self.lijsten_frame.grid_columnconfigure(1, weight=1)

        self.gebruikers_listbox = tk.Listbox(self.lijsten_frame, font=("Segoe UI", 12), bg="#23234a", fg="white")
        self.gebruikers_listbox.grid(row=0, column=0, sticky="nsew", padx=10)
        self.scenarios_listbox = tk.Listbox(self.lijsten_frame, font=("Segoe UI", 12), bg="#23234a", fg="white")
        self.scenarios_listbox.grid(row=0, column=1, sticky="nsew", padx=10)

        self.footer = tk.Label(
            self.root, 
            text="© 2025 Noodcentrale Systeem 6ICW", 
            font=("Segoe UI", 10), 
            fg="#cccccc", 
            bg="#1e1e2f"
        )
        self.footer.grid(row=4, column=0, sticky="sew", pady=10)

        self.root.bind("<Configure>", self.resize_fonts)

        # Vul de lijsten bij het starten
        self.update_lists()

    def resize_fonts(self, event):
        nieuwe_grootte = max(10, int(self.root.winfo_height() * 0.018))
        self.knop_font.configure(size=nieuwe_grootte)
        self.titel.configure(font=("Segoe UI", max(24, int(self.root.winfo_height() * 0.05)), "bold"))
        self.footer.configure(font=("Segoe UI", max(8, int(self.root.winfo_height() * 0.012))))

        knop_frame = self.add_gebruiker_knop.master
        gebruiker_breedte = knop_frame.winfo_width() // 2
        scenario_breedte = knop_frame.winfo_width() // 2
        drempelwaarde = 300
        if gebruiker_breedte < drempelwaarde:
            self.add_gebruiker_knop.config(text="➕\nVoeg \ngebruiker \ntoe")
        else:
            self.add_gebruiker_knop.config(text=self.gebruiker_tekst)
        if scenario_breedte < drempelwaarde:
            self.add_scenario_knop.config(text="🧩\nVoeg \nscenario \ntoe")
        else:
            self.add_scenario_knop.config(text=self.scenario_tekst)

    def open_gebruiker_dialog(self):
        while True:
            naam = simpledialog.askstring("Gebruiker toevoegen", "Naam:")
            if naam is None:
                return  # gebruiker annuleert
            if not naam.strip():
                self.toon_melding("Naam mag niet leeg zijn!")
                continue
            break

        while True:
            telefoon = simpledialog.askstring("Gebruiker toevoegen", "Telefoonnummer:")
            if telefoon is None:
                return  # gebruiker annuleert
            if not telefoon.isdigit():
                self.toon_melding("Telefoonnummer moet uit cijfers bestaan!")
                continue
            break

        self.controller.voeg_gebruiker_toe(naam.strip(), telefoon)
        self.update_lists()

    def open_scenario_dialog(self):
        naam = simpledialog.askstring("Scenario toevoegen", "Naam:")
        if naam:
            icoon = simpledialog.askstring("Scenario toevoegen", "Icoon-bestandsnaam:")
            if icoon:
                self.controller.voeg_scenario_toe(naam, icoon)
                self.update_lists()

    def toon_melding(self, tekst):
        messagebox.showinfo("Melding", tekst)

    def update_lists(self):
        # Haal gebruikers en scenario's op via de controller
        gebruikers = self.controller.haal_alle_gebruikers_op()
        scenarios = self.controller.haal_alle_scenarios_op()

        self.gebruikers_listbox.delete(0, tk.END)
        for gebruiker in gebruikers:
            self.gebruikers_listbox.insert(tk.END, f"{gebruiker[1]} ({gebruiker[2]})")

        self.scenarios_listbox.delete(0, tk.END)
        for scenario in scenarios:
            self.scenarios_listbox.insert(tk.END, f"{scenario[1]} [{scenario[2]}]")