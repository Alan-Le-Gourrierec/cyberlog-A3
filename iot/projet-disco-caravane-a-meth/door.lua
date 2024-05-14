function SendDoor()
    try(
        function ()
            client = mqtt.client("alan-test","test.mosquitto.org",1883,false)
        end
    )
    client:connect("","")
    client:publish("CERZEN.moteur-disco","switch-mode",mqtt.QOS0)
    client:disconnect()
end