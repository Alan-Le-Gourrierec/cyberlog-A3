try(
    function ()
        device = pwm.attach(pio.GPIO18,4,0.1)
    end,function ()end,function ()end
)

device:start()
tmr.delay(2)
device:stop()

device:start()
    device:setduty(0.9)
tmr.delay(2)
device:stop()