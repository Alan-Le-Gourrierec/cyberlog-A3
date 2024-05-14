function neo_capt()
    try(function() s = sensor.attach("DHT11", pio. GPIO4)end,function()end,function()end)
    hmin = 55
    hmax = 88 --valeurs hard-codées après éssai et constataion
    
    while true do
        try(
        function() 
            hum = s:read("humidity");
            local n = math.floor(8*(hum-hmin)/(hmax-hmin));
            local r,v,b = wheelRGB(math.floor(32+96*(hum-hmin)/(hmax-hmin)));
            for i=0,n do
                neo:setPixel(i, r,v,b);
            end
            for i=7,n,-1 do
                neo:setPixel(i, 0, 0, 0);
            end
            neo:update();
        end,
        function(where, line, error, message)
            print(message);
        end,
        function()
            tmr.delayms(500)
        end
        )
    end
end