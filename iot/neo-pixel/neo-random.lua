try(
    function ()
        neo = neopixel.attach(neopixel.WS2812B,pio.GPIO23,8)
    end,
    function (message)
        print(message)
    end
)
PATH = "test/test.txt"

for i=0,7 do
    neo:setPixel(i,Random(PATH,255),Random(PATH,255),Random(PATH,255))
end
neo:update()
tmr.delay(5)
neo:detach()