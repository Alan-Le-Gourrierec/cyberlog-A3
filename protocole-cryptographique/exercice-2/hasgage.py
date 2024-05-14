import hashlib

def CryptMessage(data):
    hasher = hashlib.new("sha256")
    
    with open(data,"rb") as file:
        chunk_size = 8192
        while chunk := file.read(chunk_size):
            hasher.update(chunk)

    fichier = open("protocole-cryptographique/exercice-2/data.txt", "a")
    print(fichier.write(hasher.hexdigest()))
    fichier.close()

print(CryptMessage("protocole-cryptographique/exercice-2/test.txt"))