------ lancement des divers capteurs avec des fonction try (ce qui permet de ne pas crash si les capteurs sont déja configuré par un programme)
try(
    function ()
    enc = encoder.attach(pio.GPIO19,pio.GPIO21,pio.GPIO4,Lecture)end,
    function (where,line,error,message) print(message) end,
    function() end
)

try(
    function ()
        ledRGB = pwm.attach(pio.GPIO18,1000,0)end,function() end, function() end
)
------

-- fonction pour mettre à jour quand la valeur change
function Lecture(dir,counter,button)
    print("direction:"..dir..",counter:"..counter..",button:"..button)
end
--

-- configuration de l'état des leds
function Bouton(b,status)
    -- nous ne intéréssons que à la parité de notre bouton : si impaire => lumière allumé de base sinon lumière éteinte 
    if b == 1 then
        if status == 0 then
            status = 1 
        else 
            status = 0
        end
        ledRGB:setduty(status)
        return status
    end
end

-- "main"
function main()
    ledRGB:start()
    status = 0
    while true do
        p,s = enc:read()
        status = Bouton(s,status)
    end
end
--