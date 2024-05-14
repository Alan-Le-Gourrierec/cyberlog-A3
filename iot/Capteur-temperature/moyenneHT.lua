try(
    function ()
        s=sensor.attach("DHT22",pio.GPIO18)
        tmr.delayms(100) --fixe pour que le capteur DHT22 fonction convenablement
    end,function () end, function () end
)

function main()
    hmin,hmax,hmoy = 100,-100,0
    tmin,tmax,tmoy = 100,-100,0
    while true do
        for i=0,5 do
            try(
                function ()
                t = s:read("temperature")
                h = s:read("humidity")
                end,
                function (where,line,error,message)
                    print(message)
                end
            )
            tmin = math.min(tmin,t)
            tmax = math.max(tmax,t)
            hmin = math.min(hmin,h)
            hmax = math.max(hmax,h)
            tmoy = tmoy + t
            hmoy = hmoy +h
            print(t,h)
            tmr.delay(10)
        end
        tmoy = tmoy / 6
        hmoy = hmoy / 6
        print("temperature "..tmoy.." "..tmin.." "..tmax)
        print("humidité "..hmoy.." "..hmin.." "..hmax)
    end
end