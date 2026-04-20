from Data.dao_salle import DataSalle
from models.salle import Salle

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
            print("données incomplet")
            return False
        if int(salle.capacite) < 1:
            print("erreur capacité invalide ")
            return False
        else:
            self.dao_salle.update_salle(salle)
            print(f"la salle,{salle.code} est modifiée")
            return True

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)
        print(f"la salle avec le code {code} est supprimée")

    def rechercher_salle(self, code):
        if code:
            salle= self.dao_salle.update_salle(code)
            if salle:
               print("la salle avec le code {code} a ete trouvee")
            else:
               print("la salle nexiste pas erreur de code")
               return None

    def recuperer_salles(self):
        return self.dao_salle.get_salles()
