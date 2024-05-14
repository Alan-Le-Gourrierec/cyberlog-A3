"""
Définition de règles coupe-feu pour interdire les paquets venant des adresses mac suspectes
"""

import os
import subprocess
from scapy.all import ARP, Ether, srp, sniff

def firewall():
    # Effacement de toutes les règles de coupe-feu
    subprocess.run("arptables -F",shell=True)
    
    # Récupération des @ malicieuses repérés
    f = open("malicious.txt",'r')
    maliciousMac = f.read().split("\n")
    f.close()

    for mac in maliciousMac:
        if mac=="": # Cas où il y a une adresse mac vide dans le fichier
            continue
        # On fait un coupe-feu pour bloquer tous les paquets venant de l'adresse mac spécifié, qui sont en mode reply, c'est à dire "is-at" dans les paquets ARP
        command = "sudo arptables -A INPUT --source-mac "+str(mac)+" --opcode REPLY -j DROP"
        print("     -->",command)

if __name__=="__main__":
    print("[*] Filtrage des paquets entrant (refuse les paquets venant des adresses suspectes trouvees)")
    firewall()

