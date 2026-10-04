import customtkinter as ctk
import customtkinter as ctk
import pyperclip
import json
import os

# Configuration du design
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

fenetre = ctk.CTk()
fenetre.title("ClipFlow")
fenetre.geometry("400x600")

# Titre
titre = ctk.CTkLabel(fenetre, text="Historique ClipFlow", font=("Arial", 20, "bold"))
titre.pack(pady=15)

# Création de la zone défilante (Scrollable Frame)
zone_historique = ctk.CTkScrollableFrame(fenetre, width=350, height=450)
zone_historique.pack(pady=10)

def copier_texte(texte_complet, bouton, texte_affiche):
    # 1. On envoie le texte dans le presse-papier
    pyperclip.copy(texte_complet)
    
    # 2. Retour visuel : texte modifié et bordure verte
    bouton.configure(text="Copié ! ✓", text_color="#28a745", border_color="#28a745")
    
    # 3. Le chronomètre : retour à la normale après 1 seconde (1000 ms)
    bouton.after(1000, lambda: bouton.configure(text=texte_affiche, text_color="black", border_color="#979da2"))

def vider_historique():
    # 1. On vide le fichier physique (on remplace par une liste vide)
    fichier = "history.json"
    if os.path.exists(fichier):
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump([], f)
            
    # 2. On vide l'interface graphique
    # winfo_children() récupère tous les boutons actuellement dans la zone
    for widget in zone_historique.winfo_children():
        widget.destroy()

def charger_historique():
    fichier = "history.json"
    
    # On vérifie si le fichier existe
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            try:
                historique = json.load(f)
                
                # On lit la liste à l'envers (reversed) pour afficher les copies les plus récentes en haut
                for entree in reversed(historique):
                    texte = entree["contenu"]
                    
                    # On crée un bouton pour chaque texte.
                    # S'il est trop long, on le coupe à 50 caractères avec "..." pour ne pas casser l'affichage
                    texte_affiche = texte[:50] + "..." if len(texte) > 50 else texte
                    
                    bouton = ctk.CTkButton(
                        zone_historique, 
                        text=texte_affiche,
                        fg_color="transparent", # Fond transparent
                        text_color="black",     # Texte noir pour le mode clair
                        border_width=1,         # Petite bordure pour délimiter
                        border_color="#979da2", # Couleur de bordure par défaut (gris)
                        anchor="w"              # "w" pour West (alignement du texte à gauche)
                    )

                    # On relie le bouton à notre fonction d'action
                    bouton.configure(command=lambda t=texte, b=bouton, ta=texte_affiche: copier_texte(t, b, ta))
                    
                    # fill="x" permet au bouton de prendre toute la largeur disponible
                    bouton.pack(pady=5, padx=10, fill="x") 
                    
            except json.JSONDecodeError:
                pass # Si le fichier est vide ou corrompu, on ne fait rien

# On exécute la fonction au lancement de la fenêtre
charger_historique()

# --- AJOUT DU BOUTON DE NETTOYAGE ---
bouton_purge = ctk.CTkButton(
    fenetre,
    text="Vider l'historique 🗑️",
    fg_color="#dc3545",      # Rouge alerte
    hover_color="#c82333",   # Rouge un peu plus foncé au survol
    command=vider_historique
)
bouton_purge.pack(pady=10)

# Lancement de l'interface
fenetre.mainloop()