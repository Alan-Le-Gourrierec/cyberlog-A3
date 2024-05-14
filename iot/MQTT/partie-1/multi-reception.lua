try(function ()
    client = mqtt.client("alan-test","test.mosquitto.org",1883,false)
end,
function(message) 
    print(message)
end)

client:connect("","")

function Reception(len,message)
    console("MASTER"..message)
end

function Devoir(len,message)
    console("devoir MASTER"..message)
end

function etudiant(len,message)
    console("etudiant"..message)
end

client:subscribe("MASTER",mqtt.QOS0, Reception)
client:subscribe("devoir MASTER",mqtt.QOS0, Devoir)
client:subscribe("etudiant",mqtt.QOS0, etudiant)
