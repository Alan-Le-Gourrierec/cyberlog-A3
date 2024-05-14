client=mqtt.client("temp","test.mosquitto.org",1883,false)
tmr.delay(1)
client:connect(",")

temp_max=-1
lieu_max="?"

temp_min=200
lieu_min="?"

function Recep_temp()
    debut,fin=Ch:find(":")
    nom=Ch:sub(0,debut-1)
    temp=tonumber(ch:sub(fin+1))
    if temp>temp_max then temp_max = temp; lieu_max = nom end
    if temp<temp_min then temp_min = temp; lieu_min = nom end
end

client: subscribe("temp",mqtt.QOS0,Recep_temp)