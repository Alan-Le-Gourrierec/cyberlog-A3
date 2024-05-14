try(function ()
        client = mqtt.client("MASTER","test.mosquitto.org",1883,false)
    end,
    function (message)
        print(message)
    end
)

client:connect("","")

function Reception(len,message)
    if message == "alerte" then
        s = servo.attach(pio.GPIO23)
        s:write(180)
        tmr.delay(2)
        s:detach()
    elseif message == "stop" then
        s = servo.attach(pio.GPIO23)
        s:write(0)
        tmr.delay(2)
        s:detach()
    end
end

client:subscribe("signal",mqtt.QOS0, Reception)