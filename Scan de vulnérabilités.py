import os
import datetime

#demande l'ip de la machine à scanner
ip = input("Veuillez entrer l'adresse IP de la machine que vous souhaitez scanner : ")

#execute la commande avec popen afin de permettre de mettre l'output dans le fichier rapport
commande = os.popen(f"nmap -sV --script vulners {ip}")

#nommage du fichier de rapport avec la date et heure de l'éxecution
nomRapport = "rapport" + datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + ".txt"
fichier = open(nomRapport, 'w')

#insertion de l'output de la commande dans le fichier rapport
for i in commande.readlines():
    fichier.write(i)

#fermeture du fichier
fichier.close()

#affichage du résultat du scan
os.system("type "+nomRapport)