import zlib 
import random as rd

def CRC32(message):
    return zlib.crc32(message.encode('utf-8'))

tmp = CRC32("ecureuil")

def Noise(message):
    tmp = [bin(ord(char))[2:] for char in message]
    
def Check(message, reception)

print(Noise('ecureuil'))
    