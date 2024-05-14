from scapy.all import *
import socket

#logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

Host = "192.168.102.182"
Port = 12345

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind(( Host,Port))
socket.listen(1)

client, ip = socket.accept()
print("Connexion ouverte avec",ip)

while(True):
    requete_client = client.recv(1000)
    requete_client = requete_client.decode()
    print(requete_client)
    if not requete_client:
        print("Au revoir")
        client.close()
        socket.close()
        break
    message = input(">")
    message = message.encode()
    client.send(message)
