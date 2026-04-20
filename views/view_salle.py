import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")
        self.geometry("600x600")
        self.service_salle = ServiceSalle()

        self.cadreInfo = ctk.CTkFrame(self)
        self.cadreInfo.pack(pady=10)
        self.entry_code = ctk.CTkEntry(self.cadreInfo, placeholder_text="Code")
        self.entry_code.pack(pady=5)
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo, placeholder_text="Libelle")
        self.entry_libelle.pack(pady=5)
        self.entry_type = ctk.CTkEntry(self.cadreInfo, placeholder_text="Type")
        self.entry_type.pack(pady=5)
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, placeholder_text="Capacite")
        self.entry_capacite.pack(pady=5)

        self.cadreBtn = ctk.CTkFrame(self)
        self.cadreBtn.pack(pady=10)
        ctk.CTkButton(self.cadreBtn, text="Ajouter", command=self.ajouter_salle).pack(pady=5)
        ctk.CTkButton(self.cadreBtn, text="Modifier", command=self.modifier_salle).pack(pady=5)
        ctk.CTkButton(self.cadreBtn, text="Supprimer", command=self.supprimer_salle).pack(pady=5)
        ctk.CTkButton(self.cadreBtn, text="Rechercher", command=self.rechercher_salle).pack(pady=5)