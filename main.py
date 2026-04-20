from Data.dao_salle import DataSalle
from models.salle import Salle
from services.services_salle import ServiceSalle
import mysql.connector
'''
dao=DataSalle()
try:
    con = dao.get_connection()
    print("connexion effectuée")
    con.close()
except Exception as e:
    print("pas de connexion", e)

s1= Salle("C211", "Informatique" , "salle_cours", 30)
s2= Salle("C234", "medecine" , "laboratoire", 25)
s3= Salle("C401", "etudes" , "librairie", 2)
s4= Salle("C314", "aide_sociale" , "auditaurium", 80)

try:
    dao.insert_salle(s1)
    print(f"la salle {s1.code} ajoutée")
    dao.insert_salle(s2)
    print(f"la salle {s2.code} ajoutée")
    dao.insert_salle(s3)
    print(f"la salle {s3.code} ajoutée")
    dao.insert_salle(s4)
    print(f"la salle {s4.code} ajoutée")
except Exception as e:
    print("pas d'insertion", e)

print("\n")
dao.delete_salle("C401")
print(f" la salle C401 a ete supprimer")

print("\n")
s4_mod=Salle("C314", "aide_sociale" , "auditaurium", 80)
dao.update_salle(s4_mod)
print(f" la salle C314 a ete modifiée")

print("\n")
recherche =dao.get_salle("C455")
if recherche:
    print("la salle C455 a ete trouve ")
    print(f"ses informations sont:" )
    recherche.afficher_infos()
else:
    print("la salle C455 n' exixte pas")  

print("\n Liste des salles")     
salles = dao.get_salles()
for salle in salles:
    salle.afficher_infos() 
'''
service = ServiceSalle()

print("\n1. Liste des salles")
salles = service.recuperer_salles()
for s in salles:
    s.afficher_infos()
s6 = Salle("C304","Appui tech","Laboratoire",35)
print("\n2. Ajouter salle")
#service.ajouter_salle(s6)
#print(message)
print("\n3. Modification salle C303")
salle = service.rechercher_salle("C303")
if salle:
    salle.capacite= 50
    salle.libelle = "chimie"
    salle.type = "cours"
    service.modifier_salle(salle)
    print("la salle la salle C303 a ete modifie ")
print("\n4. Suppression C485")
if service.rechercher_salle("C485"):
    service.supprimer_salle("C485")
    #print("Salle supprimée")
#else:
#    print("Salle inexistante")
print("\n5. Recherche C404")
recherche = service.rechercher_salle("C404")

if recherche:
    recherche.afficher_infos()
else:
    print("Salle non trouvée")
print("\nListe finale :")
salles = service.recuperer_salles()
for s in salles:
    s.afficher_infos()

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()




