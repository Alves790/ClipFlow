import pyperclip
import time
import json
import os
from datetime import datetime

def sauvegarder_copie(texte):
    fichier = "history.json"
    historique = []
    
    # Étape 1 : Si le fichier existe déjà, on récupère son contenu pour ne rien écraser
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            # On lit le JSON et on le transforme en liste Python
            try:
                historique = json.load(f)
            except json.JSONDecodeError:
                historique = [] # Sécurité si le fichier est corrompu ou vide
                
    # Étape 2 : On crée une sorte de carte d'identité pour notre nouveau texte
    nouvelle_entree = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "contenu": texte
    }
    
    # On ajoute cette nouvelle entrée à notre liste
    historique.append(nouvelle_entree)
    
    # Étape 3 : On réécrit le fichier avec la liste mise à jour
    with open(fichier, "w", encoding="utf-8") as f:
        # indent=4 permet de formater le fichier pour qu'il soit lisible par un humain
        json.dump(historique, f, indent=4, ensure_ascii=False)

print("> Moteur d'écoute activé. En attente de nouvelles copies...")
print("> (Appuie sur Ctrl+C dans ce terminal pour l'arrêter)")

# On enregistre ce qu'il y a actuellement pour ne pas réagir au passé
last_copied = pyperclip.paste()

try:
    while True:
        # On lit le presse-papier à l'instant T
        current_copied = pyperclip.paste()
        
        # Si le texte est nouveau ET qu'il n'est pas vide
        if current_copied != last_copied and current_copied != "":
            print("\n[NOUVELLE COPIE] :", current_copied)
            sauvegarder_copie(current_copied)
            
            # On met à jour notre mémoire avec ce nouveau texte
            last_copied = current_copied
            
        # On met le programme en pause pendant 0.5 secondes
        time.sleep(0.5)

except KeyboardInterrupt:
    # Si tu appuies sur Ctrl+C, on gère l'arrêt proprement
    print("\n> Arrêt du moteur d'écoute.")