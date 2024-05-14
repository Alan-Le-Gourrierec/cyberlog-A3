function SendDisco()
    try(
        function ()
            client = mqtt.client("alan-test","test.mosquitto.org",1883,false)
        end
    ) 
    client:connect("","")
    client:publish("CERZEN-disco","switch",mqtt.QOS0)
    client:disconnect()
end