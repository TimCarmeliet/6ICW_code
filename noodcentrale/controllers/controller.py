#REVIEW1 = we immporteren geen variabelen uit een andere klasse!  Dit botst tegen ENCAPSULATIE.
#TO DO model als attribuut instellen via de constructor (methode init), op een soortgelijke manier als de view.
from models.db_model import db

#REVIEW 2: Het is flexibeler om te werken met compositie op vlak van controllers => ACTIE = zet die hiërarchie op voor de controllers
#1 hoofdcontroller die we gaan koppelen aan de view van onze toepassing
#2 subcontrollers die overerven EN elk 1 verantwoordelijkheid hebben => 1 subcontroller voor gebruikers; 1 subcontroller voor scenario

class NoodcentraleController: #deze kan de hoofdcontroller zijn 
    def __init__(self, view): #REVIEW 3: argument model te voorzien om te weten welke db_model je wil gebruiken
        self.view = view 
        #REVIEW 4: twee bijkomende attributen maken om de 2 subcontrollers mee te initialiseren
        #bijv self.__persoon_ctrl = PersoonController()

    #REVIEW 5: getters voorzien voor view, model, de 2 extra attributen

    #TO DO bij verdere uitbreiding: Alle methoden die beide controllers nodig hebben voorzie je zeker in de hoofdcontroller 

    #in de subcontroller voorzie je dan overerving naar de NoodcentraleController => zie REVIEW 2
    #onderdeel subcontroller gebruiker
    def voeg_gebruiker_toe(self, naam, telefoon_nummer):
        db.add_user(naam, telefoon_nummer)
        self.view.toon_melding("Gebruiker toegevoegd!")

    #onderdeel subcontroller scenario
    def voeg_scenario_toe(self, naam, icoon):
        db.add_scenario(naam, icoon)
        self.view.toon_melding("Scenario toegevoegd!")

    #onderdeel subcontroller gebruiker
    def haal_alle_gebruikers_op(self):
        return db.get_all_users()

    #onderdeel subcontroller scenario
    def haal_alle_scenarios_op(self):
        return db.get_all_scenarios()
