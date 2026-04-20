import json
import mysql.connector

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

    def update_salle(self, salle):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute=("Update Salle SET libelle=%s, type=%s, capacite=%s where code=%s",
                  (salle.code, salle.libelle, salle.type, salle.capacite)
                     )
        con.commit()
        crs.close()
        con.close()
    def delete_salle(self, code):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute("DELETE FROM salle WHERE code = %s", (code,))
        print(f"la salle avec le code {code} est supprimée")
        con.commit()
        crs.close()
        con.close()
    def get_salle(self, code):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute("select * from salle where code = %s", (code,))
        row = crs.fetchone()
        con.commit()
        crs.close()
        con.close()
        if row:
            return Salle(*row)
        else:
            return None
    def get_salles(self):
        con = self.get_connection()
        crs = con.cursor()
        crs.execute("select * from Salle")
        results = crs.fetchall()
        salles = []
        for row in results:
            salles.append(Salle(*row))
        con.commit()
        crs.close()
        con.close()
        return salles