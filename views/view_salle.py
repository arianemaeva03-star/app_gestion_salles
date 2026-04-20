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

        self.cadreList = ctk.CTkFrame(self)
        self.cadreList.pack(pady=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "libelle", "type", "capacite"), show="headings")
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLE")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITE")
        self.treeList.pack(fill="both", expand=True)
        self.lister_salles()

    def ajouter_salle(self):
        s = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            int(self.entry_capacite.get())
        )
        self.service_salle.ajouter_salle(s)
        self.lister_salles()

    def modifier_salle(self):
        s = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            int(self.entry_capacite.get())
        )
        self.service_salle.modifier_salle(s)
        self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()
        self.service_salle.supprimer_salle(code)
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        s = self.service_salle.rechercher_salle(code)
        if s:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, s.libelle)
            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, s.type)
            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, s.capacite)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))

