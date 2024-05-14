msg = "ecureil:49.3"
debut,fin = msg:find(":") --définition du spéarateur

ch:sub(0,debut-1)
sh:sub(fin+1)

ch:sub(fin+1)