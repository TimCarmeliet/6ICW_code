#REVIEW 2: Het is flexibeler om te werken met compositie op vlak van controllers => ACTIE = zet die hiërarchie op voor de controllers
#1 hoofdcontroller die we gaan koppelen aan de view van onze toepassing
#2 subcontrollers die overerven EN elk 1 verantwoordelijkheid hebben => 1 subcontroller voor gebruikers; 1 subcontroller voor scenario

class NoodcentraleController: #deze kan de hoofdcontroller zijn 
    def __init__(self, view, model): #REVIEW 3: argument model te voorzien om te weten welke db_model je wil gebruiken
        self.__view = view 
        self.__model = model
        self.__persoon_ctrl = GebruikerController()
        self.__scenario_ctrl = ScenarioController()
    
    #VIEW
    def get_view(self):
        return self.__view        
    

    #MODEL
    def get_model(self):
        return self.__model


    #PERSOON_CTRL
    def get_persoon_ctrl(self):
        return self.__persoon_ctrl

    #SCENARIO_CTRL
    def get_scenario_ctrl(self):
        return self.__scenario_ctrl   

class GebruikerController(NoodcentraleController):
    def __init__(self, view, model):
        super().__init__(view, model)

    def voeg_gebruiker_toe(self, naam, telefoon_nummer):
        self.get_model().add_user(naam, telefoon_nummer)
        self.get_view().toon_melding("Gebruiker toegevoegd!")

    def haal_alle_gebruikers_op(self):
        return self.get_model().get_all_users()
        

class ScenarioController(NoodcentraleController):
    def __init__(self, view, model):
        super().__init__(view, model)

    def voeg_scenario_toe(self, naam, icoon):
        self.get_model().add_scenario(naam, icoon)
        self.get_view().toon_melding("Scenario toegevoegd!")

    def haal_alle_scenarios_op(self):
        return self.get_model().get_all_scenarios()
