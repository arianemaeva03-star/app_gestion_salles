from Data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            print("toutes les donnéés doivent etres remplis")
            return False
        if int(salle.capacite) < 1:
            print("Capacité doit etre minimum 1")
            return False
        else:
            self.dao_salle.insert_salle(salle)
            print(f"la salle {salle.code} est ajoutée")
            return True

    def modifier_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or not salle.capacite:
            print("données pas complete")
            return False
        if int(salle.capacite) < 1:
            print("erreur capacité invalide ")
            return False
        else:
            self.dao_salle.update_salle(salle)
            print(f"la salle,{salle.code} est modifiée")
            return True