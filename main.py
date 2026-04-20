from Data.dao_salle import DataSalle
from models.salle import Salle
data=DataSalle()
try:
    con = data.get_connection()
    print("connexion effectuée")
    con.close()
except Exception as e:
    print("pas de connexion", e)

