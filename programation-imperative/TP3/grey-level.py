import ImagesUtils as img

def ConvertToGrey(M):
    m,n = img.get_height(M),img.get_width(M)
    Tmp = img.empty_img(n,m)
    for i in range(n):
        for j in range(m):
            p = 0.299*M[i,j,0] + 0.587*M[i,j,1] + 0.114*M[i,j,2]
            Tmp[i,j,0] = p
            Tmp[i,j,1] = p
            Tmp[i,j,2] = p
    return Tmp

img.write_img('programation-imperative/TP3/testgrey.png',ConvertToGrey(img.read_img('programation-imperative/TP3/TUX.png')))
img.display_img(ConvertToGrey(img.read_img('programation-imperative/TP3/TUX.png')))