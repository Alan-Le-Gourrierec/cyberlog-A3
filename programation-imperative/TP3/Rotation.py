import ImagesUtils as img 

def Miroire(M):
    m,n = img.get_height(M),img.get_width(M)
    Tmp = img.empty_img(m,n)
    for i in range(n):
        for j in range(m):
            for k in range(3):
                Tmp[j,i,k]=M[i,j,k]
    return Tmp

def Rotation90(M):
    m,n = img.get_height(M),img.get_width(M)
    Tmp = img.empty_img(m+1,n)
    for i in range(n):
        for j in range(m):
                Tmp[m-j,i]=M[i,j]
    return Tmp

def Rotation270(M):
    for i in range(3):
        M = Rotation90(M)
    return M

img.write_img('programation-imperative/TP3/testrot90.png',Rotation90(img.read_img('programation-imperative/TP3/TUX.png')))
img.display_img(Rotation90(img.read_img('programation-imperative/TP3/TUX.png')))

img.write_img('programation-imperative/TP3/testrot270.png',Rotation270(img.read_img('programation-imperative/TP3/TUX.png')))
img.display_img(Rotation270(img.read_img('programation-imperative/TP3/TUX.png')))