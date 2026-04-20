import json
import mysql.connector
from mysql.connector import cursor

from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("./Data/config.json", "r", encoding="utf-8") as f:
             config = json.load(f)
        con=mysql.connector.connect(host=config["host"], user=config["user"],
                                    password=config["password"], database=config["database"])
        return con

    def insert_salle(self, salle):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute("insert into Salle values(%s,%s,%s,%s)",
                    (salle.code, salle.libelle, salle.type, salle.capacite)
                    )
        con.commit()
        crs.close()
        con.close()

