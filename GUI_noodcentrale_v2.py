import tkinter as tk
from tkinter import ttk

class NoodcentraleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Noodcentrale")

        # Venster volledig scherm
        scherm_breedte = self.root.winfo_screenwidth()
        scherm_hoogte = self.root.winfo_screenheight()
        self.root.geometry(f"{scherm_breedte}x{scherm_hoogte}")

        # Kleuren en stijl
        self.root.configure(bg="#1e1e2f")
        stijl = ttk.Style()
        stijl.configure("TButton", font=("Segoe UI", 16), padding=10)
        stijl.map("TButton", background=[("active", "#3e3e5e")])

        # Hoofdtitel
        titel = tk.Label(
            self.root, 
            text="🚨 Noodcentrale", 
            font=("Segoe UI", 32, "bold"), 
            fg="white", 
            bg="#1e1e2f"
        )
        titel.pack(pady=50)

        # Frame voor knoppen
        knop_frame = tk.Frame(self.root, bg="#1e1e2f")
        knop_frame.pack(expand=False) # Frame is zo groot als de inhoud, niet groter dan dat

        # Knoppen
        self.add_gebruiker_knop = ttk.Button(knop_frame, text="➕ Voeg gebruiker toe")
        self.add_gebruiker_knop.grid(row=0, column=0, padx=30, pady=20)

        self.add_scenario_knop = ttk.Button(knop_frame, text="🧩 Voeg scenario toe")
        self.add_scenario_knop.grid(row=0, column=1, padx=30, pady=20)

        # Footer
        footer = tk.Label(
            self.root, 
            text="© 2025 Noodcentrale Systeem 6ICW", 
            font=("Segoe UI", 10), 
            fg="#cccccc", 
            bg="#1e1e2f"
        )
        footer.pack(side="bottom", pady=20)


# Main programma
if __name__ == "__main__":
    root = tk.Tk()
    app = NoodcentraleGUI(root)
    root.mainloop()
