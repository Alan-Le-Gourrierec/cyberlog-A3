import hashlib

def Hash(monFichier):
    with open(monFichier, "rb") as file:
        data = file.read()
        hash = hashlib.sha256()
        hash.update(data)
        empreinte = hash.hexdigest()
    return empreinte

testFile = 'histoire.txt'
empreinteFile = 'empreinte.txt'

empreinte = Hash(testFile)
print(len(empreinte))

with open(empreinteFile, "w") as file:
    file.write(empreinte)

print(Hash('protocole-cryptographique/1.pdf'))
print(Hash('protocole-cryptographique/2.pdf'))
print(Hash("protocole-cryptographique/1.pdf") == Hash("protocole-cryptographique/2.pdf"))