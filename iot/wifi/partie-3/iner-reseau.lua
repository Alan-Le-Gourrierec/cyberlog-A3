<h1> Liste des reseau </h1>

<?lua
    -- ceci est une fonction que j'avais fait précédement qui print les reseau tant qu'il y en a avec du try catch 
    condition = true
    while condition == true do
        try(
            function ()
                print(w[0].ssid.."\n")
                i = i + 1
            end,
            function () --condition d'arret => quand erreur on arret :) 
                condition = false
            end
        )
    end
?>