import pyperclip
import time

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
            
            # On met à jour notre mémoire avec ce nouveau texte
            last_copied = current_copied
            
        # On met le programme en pause pendant 0.5 seconde
        time.sleep(0.5)

except KeyboardInterrupt:
    # Si tu appuies sur Ctrl+C, on gère l'arrêt proprement
    print("\n> Arrêt du moteur d'écoute.")