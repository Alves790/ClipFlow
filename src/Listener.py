import pyperclip
import time
import storage # On importe notre nouveau cerveau de données !

print("> Moteur d'écoute activé. En attente de nouvelles copies...")
print("> (Appuie sur Ctrl+C dans ce terminal pour l'arrêter)")

last_copied = pyperclip.paste()

try:
    while True:
        current_copied = pyperclip.paste()
        
        if current_copied != last_copied and current_copied != "":
            print("\n[NOUVELLE COPIE] :", current_copied)
            
            # Le listener ne gère plus le JSON, il passe juste le relais au module storage
            storage.sauvegarder_copie(current_copied)
            
            last_copied = current_copied
            
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n> Arrêt du moteur d'écoute.")