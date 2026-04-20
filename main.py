from Data.dao_salle import DataSalle
from models.salle import Salle
dao=DataSalle()
try:
    con = dao.get_connection()
    print("connexion effectuée")
    con.close()
except Exception as e:
    print("pas de connexion", e)

s1= Salle("C208", "Informatique" , "salle_cours", 30)
s2= Salle("C234", "medecine" , "laboratoire", 25)
s3= Salle("C401", "etudes" , "librairie", 2)
s4= Salle("C314", "aide_sociale" , "auditaurium", 80)

dao.insert_salle(s1)
dao.insert_salle(s2)
dao.insert_salle(s3)
dao.insert_salle(s4)






