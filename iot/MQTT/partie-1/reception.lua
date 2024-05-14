try(function ()
    client = mqtt.client("alan-test","test.mosquitto.org",1883,false)
end,
function(message) 
    print(message)
end)

client:connect("","")

function Reception(len,message)
    console(message)
end

client:subscribe("MASTER",mqtt.QOS0, Reception)
