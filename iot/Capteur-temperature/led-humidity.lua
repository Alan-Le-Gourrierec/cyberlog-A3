try(
    function ()
        s = sensor.attach("DHT22",pio.GPIO18)end,function ()end, function () end
)

function Moyenne(iteration,moyenne,h)
    return (iteration*moyenne + h)/(iteration+1)
end

function Blink(moyenne,h)
    if h>moyenne then
        for i=0,5 do
            ledon()
            tmr.delayms(50)
            ledoff()
            tmr.delayms(50)
        end
    else
        tmr.delayms(500)
    end
end

function main()
    i,moyenne = 0,0
    while true do
        try(function ()
            h = s:read("humidity")
            moyenne = Moyenne(i,moyenne,h)
            i = i + 1
        end,
        function (where,line,error,message)
            print(message)
        end,
        function ()
            Blink(moyenne,h)
        end
        )
    end
end
