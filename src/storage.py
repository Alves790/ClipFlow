import json
import os
from datetime import datetime

FICHIER = "history.json"

def charger_historique():
    """Lit le fichier JSON et retourne la liste des copies."""
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def sauvegarder_copie(texte):
    """Ajoute une nouvelle copie au fichier JSON."""
    historique = charger_historique()
    
    nouvelle_entree = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "contenu": texte,
        "epingle": False  # Préparation pour ta future fonctionnalité
    }
    
    historique.append(nouvelle_entree)
    
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(historique, f, indent=4, ensure_ascii=False)

def purger_historique():
    """Écrase le fichier avec une liste vide."""
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump([], f)