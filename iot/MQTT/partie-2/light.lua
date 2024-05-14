try(function ()
        client = mqtt.client("MASTER","test.mosquitto.org",1883,false)
    end,
    function (message)
        print(message)
    end
)

client:connect("","")

-- c'est vraiment beaucoup mieu avec le buzzer 

function Reception(len,message)
    if message == "alerte" then
        ledon()
    elseif message == "stop" then
        ledoff()
    end
end

client:subscribe("signal",mqtt.QOS0, Reception)