try(function ()
    s = sensor.attach("DHT22",pio.GPIO4)
    tmr.delayms(90)
end)

function Gettemp()
    while true do
        try(function ()
            print("Temperature : "..s:read("temperature").." Humitité : "..s:read("humidity"))
        end,
        function (where,line,error,message)
            print(message)
        end,
        function ()
            tmr.delayms(500)
        end
        )
    end
end