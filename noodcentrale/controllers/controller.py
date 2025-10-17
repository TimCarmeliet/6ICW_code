from models.db_model import db

class NoodcentraleController:
    def __init__(self, view):
        self.view = view

    def voeg_gebruiker_toe(self, naam, telefoon_nummer):
        db.add_user(naam, telefoon_nummer)
        self.view.toon_melding("Gebruiker toegevoegd!")

    def voeg_scenario_toe(self, naam, icoon):
        db.add_scenario(naam, icoon)
        self.view.toon_melding("Scenario toegevoegd!")

    def haal_alle_gebruikers_op(self):
        return db.get_all_users()

    def haal_alle_scenarios_op(self):
        return db.get_all_scenarios()
