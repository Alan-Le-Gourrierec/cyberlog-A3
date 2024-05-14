import ImagesUtils as img
import random as rand

"""pour réaliser ce programme, j'ai décider, afin d'avoir un message encodé de façons discrète 
de décomposer le message en binaire et de coder le message sur la couleur bleu de notre image
car elle est la moins importante, si nous passons nôtre image en niveau de gris.
Pour résoudre ceci, il suffit simplement de soustraire l'image encrypté à l'image de base
et nous obtenons le message la ou les valeurs ne sont pas nul"""
message = "ecureuil"
TUX = img.read_img('programation-imperative/TP3/TUX.png') 

def Encryptage(message):
    A = list(message)
    Solve = []
    for i in range(len(A)):
        #convertion de message vers une chaine de nombre bianires (en char)
        Tmp = list(format(ord(A[i]), 'b'))
        for j in range(len(Tmp)):
            #conversion des char vers des int 
            Tmp[j] = int(Tmp[j])
            Solve.append(Tmp[j])
    return Solve

def EncrytImage(Message, Image):
    #dimestions de l'images
    CopyImage = img.copy(Image)
    n,m = img.get_height(CopyImage),img.get_width(CopyImage)
    #définition des bones pour la génération de **l'entier** aléatoire et définition des position de début et de fin
    start = int(rand.uniform(0,n*m-9*len(Message))) #n*m-9*len(Message) => ne pas dépasser des limites de notre image
    startx,starty = start//n, start%n # définition des possition x et y de départ et d'arrivé 
    for i in range(len(Message)):
        if starty > m: #si nous arrivons au bout de la ligne nous sautons la ligne 
            starty = 0
            startx += 1
        CopyImage[startx,starty,2] -= (Message[i] + 1) #encodage du message
        starty += 1
    return CopyImage

def Substract(ImageBase , Image):
    Solve = []
    n,m = img.get_height(Image),img.get_width(Image) 
    ImageBase = img.copy(ImageBase)
    for i in range(m): #soustraction de l'image d'origine avec la nouvelle image 
        for j in range(n): #si différent de 0 => nous rangeons dans un tableau sa valeur
            if ImageBase[i,j,2] - Image [i,j,2] != 0:
                Solve.append(ImageBase[i,j,2]-Image[i,j,2]-1)
    return Solve #retour des binaires sous forme de tableau

def Decrypte(ImageBase,Imagecrypte):
    Tmp = (Substract(ImageBase,Imagecrypte))
    Solve = []
    for i in range(int(len(Tmp)/7)):
        somme = 0 
        for j in range(7):
            #conversion des binaires vers leur valeur en ASCII
            somme+=(Tmp[i*7+j] * 2 **(6-j))
        Solve.append((chr(somme))) 
    return "".join(Solve) # return du mot en format string
     
encrypted = EncrytImage(Encryptage(message),TUX)
img.write_img('programation-imperative/TP3/stegano.png',encrypted)
print(Decrypte(TUX,img.read_img('programation-imperative/TP3/stegano.png')))