try(
    function ()
        enc = encoder.attach(pio.GPIO19,pio.GPIO21,pio.GPIO18)
    end,
    function (where,line,error,message)
        print(message)
    end,
    function ()end
)

blink = function (speed)
    ledon();
    tmr.delayms(speed)
    ledoff();
    tmr.delayms(speed)
end

function speed(speedmoin1,speed,timer)
    if speedmoin1<speed then
        return timer +1
    end
    if speedmoin1>speed then
        return timer-1
    else
        return timer
    end
end

function main()
    pmoin1 = 0
    delay = 100
    while true do
    try(
        function ()
            p,s = enc:read()
            delay = speed(pmoin1,p,delay)
            print(delay)
            blink(delay)
            pmoin1 = p
        end,
        function (where,line,error,message)
            print(message)
        end,
        function ()
        end
        )
    end
end
