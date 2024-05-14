function SaveInFile(value,PATH)
    --sauvegarde de la valeur dans le fichier
    io.output(PATH)
    io.write(""..value)
    io.close()
end

function Random(PATH,modulo)
    --[[mathématiquement parlant, si nous prenons en modulo un nombre premier
    nous obteindrons forcément pour chaque itération de notre modulo (de 0 à m-1
    une valeur différente, et je me base donc sur ce principe pour la génération)]]--

    local f = assert(io.open(PATH, "r"))
    i = f:read("*all")
    m = 131071 --nombre premier (6e nombre de Mersenne)
    nbr = 22091 --autre nombre premier
    i = math.fmod(nbr*i,m)
    f:close()
    SaveInFile(i,PATH)
    return math.fmod(i,modulo)
end