try(
    function ()
        w = net.wf.scan(true)
    end,
    function (message)
        print(message)
    end
)

function Opening()
    cls()
    console("graph evolution wifi")
    tmr.delay(3)
    cls()
end

function HUD() 
    -- tracage des lignes pour le graphique de l'humidité 
    gdisplay.line({5,0},{5,55})
    gdisplay.line({0,5},{128,5})
end

function ForABetterWifi()
    i = 0
    condition = true
    max = 0
    while condition == true do    
        try(
            function ()
                max = math.max(max,math.floor(math.abs(w[i].rssi)/2))
                i = i + 1
            end,
            function ()
                condition = false
            end
        )
    end
    return max
end

function GraphWifi()
    Opening()
    HUD()
    for i=6,127 do
        print(ForABetterWifi())
        gdisplay.putpixel(i,ForABetterWifi())
        tmr.delayms(200)
    end
end
