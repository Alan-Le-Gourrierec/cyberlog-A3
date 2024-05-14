"""
Programme principal qui analyse les tables ARP et lance les coupe-feu
"""

from scapy.all import *

# Importation des programmes annexes
from filtrage import firewall 
from arpManager import *


# Analyse de la table renvoyée par la commande ARP, 
#	pour vérifier si il y a 1 @ mac pour 2 @ ip différentes
def analyseTable(listARP):
	suspicious=[]

	# On parcours la table pour voir si il existe 2 adresse ip pour une même adresse mac
	for device1 in listARP:
		for device2 in listARP:
			if device1['ip']!=device2['ip'] and device1['mac']==device2['mac']:
				susp = [device1['ip'],device2['ip'],device1['mac']]
				if sorted(susp) not in suspicious:
					print("[*] Attaque MITM ... ")
					suspicious.append(sorted(susp))
					print("		--> Suspicious",susp)
			else:
				pass

	return suspicious

# Analyse du réseau en comparant la table arp linux avec celle scapy, pour déterminer qui est l'attaquant, et qui est le bon client/serveur
def analyse():
    print("[*] Scan ARP ... ")
    table = arp_cmd()
    for device in table:
        print("      -->",device['ip']," at ",device['mac'])
    
    print("[*] Analyse de la table ARP ...")
    suspect = analyseTable(table)

    maliciousAdr = []
    goodIP = []

    for ip1,ip2,mac in suspect:
        device1 = arp_scan(ip1)[0]
        device2 = arp_scan(ip2)[0]

        if device1['mac']==mac:
            bad  = device1
            goog = device2
            maliciousAdr.append(device1)
            goodIP.append(device2)
        if device2['mac']==mac:
            bad  = device2
            good = device1
            maliciousAdr.append(device2)
            goodIP.append(device1)
        
        print("[*] 2 machines ont la même adresse MAC dans la table ARP : ")
        print("     = Attaquant :",bad['ip']," at ",bad['mac'])
        print("     = Victime   :",good['ip']," at ",good['mac'])

    # Lancement du programme de suppression des entrées ARP
    supprSuspectAdr(maliciousAdr)
    
    # On rearp avec la bonne machine
    for device in goodIP:
        reARP(device['ip'])

if __name__=="__main__":
    # Lancement du prog de comparaison pour vérifier si il y a spoof arp, toutes les 10 secondes 
    try:
        while(True):
            analyse()
            print("[*] Configuration du coupe-feu pour bloquer les adresses mac suspects")
            firewall()
            print("----------------------------------------------------------------------------\n\n")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n                   <==== Au revoir ====>\n")
