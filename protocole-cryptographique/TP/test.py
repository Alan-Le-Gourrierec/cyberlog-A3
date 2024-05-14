import zlib
import random as rd

def simulate_transmission(data):
    # simulation par ajout de hasard
    noisy_data = Noise(data) 
    print(noisy_data)
    checksum = zlib.crc32(noisy_data.encode('utf-8')) 
    
    return CRC32(data, checksum), checksum, noisy_data

def Noise(data):
    # ajout de hasard
    data = list(data)
    for i in range(len(data)-1):
        if rd.uniform(0,100)>95:
            data[i]=chr(97+rd.randint(0,25))
    return "".join(data)

def CRC32(data, checksum):
    # check le checksum pour voir si ceci correspond 
    return zlib.crc32(data.encode('utf-8')) == checksum

# Test the simulation
message = "test"
print(simulate_transmission(message))