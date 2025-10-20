import sqlite3
db_name = "noodcentrale.db"  #REVIEW1: HIER NIET INITIALISEREN

class Database:  #Opzet van deze klasse is om het database model te vormen, niet om de database te zijn => REVIEW2: WIJZIG NAAM CLASS    
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        """Maak verbinding met de database."""
        return sqlite3.connect(self.db_name)

    def create_tables(self):
        """Maak de vereiste tabellen aan als ze nog niet bestaan."""
        with self.connect() as conn:
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    naam TEXT NOT NULL,
                    telefoon_nummer TEXT UNIQUE NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS scenarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    naam TEXT NOT NULL,
                    icoon TEXT
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS scenario_users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    scenario_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    FOREIGN KEY (scenario_id) REFERENCES scenarios(id),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            conn.commit()
            #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode

    # ---------- Gebruikers ----------
    def add_user(self, naam, telefoon_nummer):
        """Voeg een nieuwe gebruiker toe."""
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO users (naam, telefoon_nummer) VALUES (?, ?)", (naam, telefoon_nummer))
            conn.commit()
        #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode

    def get_all_users(self):
        """Haal alle gebruikers op."""
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, naam, telefoon_nummer FROM users")
            return cur.fetchall()
        #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode (zet je fethall in temp variabele)


    # ---------- Scenarios ----------
    def add_scenario(self, naam, icoon):
        """Voeg een nieuw scenario toe."""
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO scenarios (naam, icoon) VALUES (?, ?)", (naam, icoon))
            conn.commit()
        #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode


    def get_all_scenarios(self):
        """Haal alle scenario's op."""
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, naam, icoon FROM scenarios")
            return cur.fetchall()
        #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode (zet je fethall in temp variabele)


    # ---------- Koppelingen ----------
    def link_user_to_scenario(self, user_id, scenario_id):
        """Koppel gebruiker aan scenario."""
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO scenario_users (user_id, scenario_id) VALUES (?, ?)",
                (user_id, scenario_id)
            )
            conn.commit()
        #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode (zet je fethall in temp variabele)

    def get_users_for_scenario(self, scenario_id):
        """Haal alle gebruikers op die gekoppeld zijn aan een scenario."""
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT u.id, u.naam, u.telefoon_nummer
                FROM users u
                JOIN scenario_users su ON su.user_id = u.id
                WHERE su.scenario_id = ?
            """, (scenario_id,))
            return cur.fetchall()
    #REVIEW3: Good practice = sluit je databaseconnectie bij einde methode (zet je fethall in temp variabele)


#REVIEW4: onderstaande code helemaal in commentaar => zie unit testen om te verbeteren.
# Initialiseer de database
db = Database(db_name)
"""
# Voor directe testen, uncomment de volgende regels:
if __name__ == "__main__":
    db.add_user("Jan Jansen", "0612345678")
    db.add_scenario("Brand", "brand_icoon.png")
    users = db.get_all_users()
    scenarios = db.get_all_scenarios()
    print("Users:", users)
    print("Scenarios:", scenarios)
    if users and scenarios:
        db.link_user_to_scenario(users[0][0], scenarios[0][0])
        linked_users = db.get_users_for_scenario(scenarios[0][0])
        print("Linked Users for Scenario 'Brand':", linked_users)
        """