from Data.dao_salle import DataSalle
from models.salle import Salle
data=DataSalle()
try:
    con = data.get_connection()
    print("connexion effectuée")
    con.close()
except Exception as e:
    print("pas de connexion", e)

s1= Salle(208, "Informatique" , "salle_cours", 30)
s2= Salle(234, "medecine" , "laboratoire", 25)
s3= Salle(401, "etudes" , "librairie", 2)
s4= Salle(314, "aide_sociale" , "auditaurium", 80)
try:
   data.insert_salle(s1)
   print(f"la salle dont le code est {s1.code}, est ajoutée")
except Exception as e:
   print("class pas inserée")

