--même programme que pour ke chapitre 17 : application
try(function () -- fonction teste
    s = sensor.attach("DHT22",pio.GPIO2)
    tmr.delayms(200)
    temp = s:read("temperature") -- je n'ai pas compris pour quoi mais le capteur ne marchais plus
end)

try(function () --fonction teste
    client = mqtt.client("alan-test","test.mosquitto.org",1883, false)
end)


nom = "Cerzen"
try(function ()

    client:connect("","")
    client:publish("temp",nom.." "..temp,mqtt.QOS0)
    client:disconnect()
end)

os.sleep(10)