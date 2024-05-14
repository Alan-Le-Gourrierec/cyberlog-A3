"""
Programme contenant tous les programmes en lien avec ARP (scan, ping en broadcast)    
"""

import os
import subprocess
from scapy.all import Ether, srp, ARP

# Ajouter une fonction pour reARP, refaire la liaison avec le bon serveur, sans passer par l'attaquant
def reARP(ipdst):
	arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ipdst)
	arp_packet.show()
	# On envoie 10 paquet 
	for i in range(5):
		msg = srp(arp_packet, timeout=10, verbose=False)
	return msg

# Permet de supprimer les adresses suspectées d'arpSpoofing de la table arp de l'hôte
def supprSuspectAdr(maliciousMac):
    # on ouvre un fichier qui contiendra les adresses mac malicieuses
    f = open("malicious.txt","w")
    
    for device in maliciousMac:
        a = input("[*] Do you want to delete "+str(device)+"? (Y/n)")
        match a:
            case 'n':
                pass
            case _  :
                print("[*] Removing from arp table ...")
                # On supprime la ligne de la table arp en rapport avec l'adresse mac malicieuse
                subprocess.run(['sudo','arp','-d',device['ip']], stdout=subprocess.PIPE, text=True)
                # On ajoute l'adresse malicieuse dans le fichier
                f.write(str(device['mac'])+"\n")
    f.close()

# Scan une adresse ip du réseau, et renvoie la table arp correspondante
# 	Il est aussi possible de scanner un réseau en mettant le nom du réseau à la place de 'ip' 
# 	ex : 10.0.0.1/24 -> qui scan les ip de 10.0.0.1 à 10.0.0.255
def arp_scan(ip):
    # Créer une trame ethernet avec une requete ARP
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    # Envoye la trame ARP et recevoie la reponse 
    result = srp(arp_request, timeout=3,verbose=0)[0]

    # Analyser la reponse pour obtenir la table ARP
    arp_table=[]
    for sent, received in result:
        arp_table.append({'ip': received.psrc, 'mac': received.hwsrc})

    return arp_table

# Recuperation du scan arp, via la commande `arp`
#   car il y a une différence entre la table arp linux et scapy
def arp_cmd():
	os.system("arp -a > tableARP.txt")

	# ouverture du fichier qui contient la table ARP
	f = open("tableARP.txt", 'r')
	table = f.read().split("\n")
	f.close

	listARP = []

	# On traite le fichier pour resortir un dictionnaire contenant les ip et mac en valeurs.
	try:
		for device in table:
			info = device.split(' ')
			ip=info[1][1:-1]
			mac=info[3]
			listARP.append({'ip':ip,'mac':mac})

	except IndexError:
		pass

	return listARP
