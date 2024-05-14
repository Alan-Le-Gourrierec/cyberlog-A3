try(
    function ()
        neo = neopixel.attach(neopixel.WS2812B,pio.GPIO22,8)
    end,
    function (message)
        print(message.."NEO")
    end
)
try(
    function ()
        w = net.wf.scan(true)
    end,
    function (message)
        print(message.."WIFI")
    end
)
function clear()
    for i=0,7 do
        neo:setPixel(i,0,0,0)
    end
    neo:update()
end

function eduroram()
    n =math.floor(math.abs(w[0].rssi/10))
    if n >= 9 then
        n = 0
    end
    if n <2 then
        n = 7
    else
        n = 8-n
    end
    console(w[0].ssid.."  "..w[0].rssi)
    clear()
    for i=0,n do
        neo:setPixel(i,0,0,20)
    end
    neo:update()
end