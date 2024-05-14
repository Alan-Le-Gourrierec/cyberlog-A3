ledon = function ()
    pio.pin.setval(1,pio.GPIO2)
end

ledoff = function ()
    pio.pin.setval(0,pio.GPIO2)
end

blink = function (n)
    for i = 1,n do
       ledon();
       tmr.delay(1)
       ledoff();
       tmr.delay(1) 
    end
end
