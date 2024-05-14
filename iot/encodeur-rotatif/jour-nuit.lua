try(
    function () encod = encoder.attach(pio.GPIO19,pio.GPIO21,pio.GPIO5,Lecture)end,function ()end,function ()end
)
try(
    function () neo=neopixel.attach(neopixel.WS2812B,pio.GPIO4)end,function() end,function() end
)
function Lecture(dir,counter,button)
    print("direction : "..dir..", conteur : "..counter..", bouton : "..button)
end

function neolight(e)
    if e == 1 then
        e = 0
    else
        e = 1
    end
    for i=0,7 do
        neo:setPixel(i,0,0,20*e) 
    end
    neo:update()
    return e
end

function day()
    while true do
        p1,s1,e = 0,0,0
        try(
            function ()
            p,s = encod:read()
            print(p,s)
            if( s ~= s1)then
                s1 = s
                e = neolight(e)
            end
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