from Data.dao_salle import DataSalle
from models.salle import Salle
import mysql.connector
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






