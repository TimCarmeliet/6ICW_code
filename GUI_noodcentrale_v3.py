import tkinter as tk
from tkinter import ttk

class NoodcentraleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Noodcentrale")

        scherm_breedte = self.root.winfo_screenwidth()
        scherm_hoogte = self.root.winfo_screenheight()
        self.root.geometry(f"{scherm_breedte}x{scherm_hoogte}")

        self.root.configure(bg="#1e1e2f")

        # Configureer grid van root zodat alles schaalt
        self.root.grid_rowconfigure(0, weight=1)   # Titel
        self.root.grid_rowconfigure(1, weight=2)   # Knoppen
        self.root.grid_rowconfigure(2, weight=1)   # Footer
        self.root.grid_columnconfigure(0, weight=1)

        # Hoofdtitel
        titel = tk.Label(
            self.root, 
            text="🚨 Noodcentrale", 
            font=("Segoe UI", 32, "bold"), 
            fg="white", 
            bg="#1e1e2f"
        )
        titel.grid(row=0, column=0, sticky="nsew", pady=20)

        # Frame voor knoppen
        knop_frame = tk.Frame(self.root, bg="#1e1e2f")
        knop_frame.grid(row=1, column=0, sticky="nsew")
        knop_frame.grid_columnconfigure(0, weight=1)
        knop_frame.grid_columnconfigure(1, weight=1)

        # Knoppen
        self.add_gebruiker_knop = ttk.Button(knop_frame, text="➕ Voeg gebruiker toe")
        self.add_gebruiker_knop.grid(row=0, column=0, padx=30, pady=20, sticky="ew", ipady=20)

        self.add_scenario_knop = ttk.Button(knop_frame, text="🧩 Voeg scenario toe")
        self.add_scenario_knop.grid(row=0, column=1, padx=30, pady=20, sticky="ew", ipady=20)

        # Footer
        footer = tk.Label(
            self.root, 
            text="© 2025 Noodcentrale Systeem 6ICW", 
            font=("Segoe UI", 10), 
            fg="#cccccc", 
            bg="#1e1e2f"
        )
        footer.grid(row=2, column=0, sticky="sew", pady=10)

# Main programma
if __name__ == "__main__":
    root = tk.Tk()
    app = NoodcentraleGUI(root)
    root.mainloop()