try(
    function ()
    s = sensor.attach("DHT22",pio.GPIO22)
    end
)

function GetTemp()
    return s:read("temperature")
end

function main()
    while true do
        try(
        function ()
            console(GetTemp())
        end,
        function (where,line,error,message)
            print(message)
        end,
        function ()
            tmr.delay(1)
        end
        )
    end
end