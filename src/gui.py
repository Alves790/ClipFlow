import customtkinter as ctk
import pyperclip
from src import storage

def copier_texte(texte_complet, bouton, texte_affiche):
    pyperclip.copy(texte_complet)
    bouton.configure(text="Copié ! ✓", text_color="#28a745", border_color="#28a745")
    bouton.after(1000, lambda: bouton.configure(text=texte_affiche, text_color="black", border_color="#979da2"))

class ClipFlowApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("ClipFlow")
        self.geometry("400x600")
        ctk.set_appearance_mode("light")
        
        # Titre
        self.titre = ctk.CTkLabel(self, text="Historique ClipFlow", font=("Arial", 20, "bold"))
        self.titre.pack(pady=15)
        
        # Zone défilante
        self.zone_historique = ctk.CTkScrollableFrame(self, width=350, height=450)
        self.zone_historique.pack(pady=10)
        
        # Bouton de purge
        self.bouton_purge = ctk.CTkButton(
            self,
            text="Vider l'historique 🗑️",
            fg_color="#dc3545",
            hover_color="#c82333",
            command=self.vider_historique
        )
        self.bouton_purge.pack(pady=10)
        
        # Chargement initial
        self.charger_historique()

    def charger_historique(self):
        historique = storage.charger_historique()
        
        for entree in reversed(historique):
            texte = entree["contenu"]
            texte_affiche = texte[:50] + "..." if len(texte) > 50 else texte
            
            bouton = ctk.CTkButton(
                self.zone_historique, 
                text=texte_affiche,
                fg_color="transparent",
                text_color="black",
                border_color="#979da2",
                border_width=1,
                anchor="w"
            )
            bouton.configure(command=lambda t=texte, b=bouton, ta=texte_affiche: copier_texte(t, b, ta))
            bouton.pack(pady=5, padx=10, fill="x")

    def vider_historique(self):
        storage.purger_historique()
        for widget in self.zone_historique.winfo_children():
            widget.destroy()