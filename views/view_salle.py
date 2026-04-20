import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")
        self.geometry("400x400")
        self.service_salle = ServiceSalle()

        self.frame_InfoSalle = ctk.CTkFrame(self)
        self.frame_InfoSalle.pack(pady=10, padx=10)
        self.label_code = ctk.CTkLabel(self.frame_InfoSalle, text="Code:")
        self.label_code.grid(row=0, column=0, pady=5, padx=5)
        self.entry_code = ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_code.grid(row=0, column=1, pady=5, padx=5)
        self.label_libelle = ctk.CTkLabel(self.frame_InfoSalle, text="Libellé:")
        self.label_libelle.grid(row=1, column=0, pady=5, padx=5)
        self.entry_libelle = ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_libelle.grid(row=1, column=1, pady=5, padx=5)
        self.label_type = ctk.CTkLabel(self.frame_InfoSalle, text="Type:")
        self.label_type.grid(row=2, column=0, pady=5, padx=5)
        self.entry_type = ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_type.grid(row=2, column=1, pady=5, padx=5)
        self.label_capacite = ctk.CTkLabel(self.frame_InfoSalle, text="Capacité:")
        self.label_capacite.grid(row=3, column=0, pady=5, padx=5)
        self.entry_capacite = ctk.CTkEntry(self.frame_InfoSalle)
        self.entry_capacite.grid(row=3, column=1, pady=5, padx=5)

        self.frame_Actions = ctk.CTkFrame(self)
        self.frame_Actions.pack(pady=10)
        self.btn_ajouter = ctk.CTkButton(self.frame_Actions, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, pady=10, padx=10)
        self.btn_modifier = ctk.CTkButton(self.frame_Actions, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, pady=10, padx=10)
        self.btn_supprimer = ctk.CTkButton(self.frame_Actions, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, pady=10, padx=10)
        self.btn_rechercher = ctk.CTkButton(self.frame_Actions, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, pady=10, padx=10)


        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "libelle", "type", "capacite"), show="headings")

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        self.treeList.column("code", width=50)
        self.treeList.column("libelle", width=150)
        self.treeList.column("type", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))

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

