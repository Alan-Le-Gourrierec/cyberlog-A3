try(
    function ()
        s = sensor.attach("DHT22",pio.GPIO22)
    end,
    function (message)
        print(message)
    end
)

function GetTemp()
    --lecture de l'humidité sur donnée par le capteur
    return s:read("humidity")
end

function Opening()
    cls()
    --nomage du graphique au lancement
    console("graph humidité")
    tmr.delay(2)
    cls()
end

function HUD()
    -- tracage des lignes pour le graphique de l'humidité 
    gdisplay.line({5,0},{5,55})
    gdisplay.line({0,5},{128,5})
end

function main()
    Opening()
    HUD()
    for i=6,128 do
        --bornage entre 6 et 158 pour que ca ne dépasse pas de l'écran
        gdisplay.putpixel(i,GetTemp())
        tmr.delayms(200)
    end
end