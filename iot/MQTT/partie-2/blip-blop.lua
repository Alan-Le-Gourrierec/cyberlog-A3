try(function () -- fonction testé
        client = mqtt.client("MASTER","test.mosquitto.org",1883,false)
    end, 
    function (message) --fonction en cas d'érreur
        print(message)
    end
)

client:connect("","")

function Reception(len,message)
    if message == "alerte" then
        console("blip")
    elseif message == "stop" then
        console("blop")
    end
end

client:subscribe("signal",mqtt.QOS0, Reception)
client:disconnect()