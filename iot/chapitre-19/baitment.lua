--vu que nous avons tous la flem d'executer plusieur fichier tout va être fait dans un

--connection capteur de temperature
try(
    function ()
        s = sensor.attach("DHT22",pio.GPIO23)
        tmr.delayms(200)
    end,
    function (message)
        print(message) --renvoie le message d'erreur
    end
)

print(net.stat(true)[0]["ip"]) --print l'ip dans le terminal de l'esp
net.service.http.start() --lancement serveur

--connection au serveur mqtt (dans notre cas, test.mosquitto.org, le serveur de base de test de mosquitto)
try(
    client = mqtt.client("MASTER",test.mosquitto.org,1883)
    tmr.delayms(200)
    client.connect("","")
)

--initialisation des variables 
temp_max = -20; lieu_max = "?" 
temp_min = 200; lieu_min = "?"

function Temperature(len,output)
    debut,fin=output:find(':')
    name = output:sub(0,debut-1) --reception du nom du lieu 
    temp = tonumber(output:sub(fin+1)) --conversion en number
    if temp < tmep_min then 
        temp_min = temp; lieu_min = name end
    if  temp > temp_max then
        temp_max = temp; lieu_max = name end
    print("maximum : "..lieu_max.." : "..temp_max)
    print("minimum : "..lieu_min.." : "..temp_min)
    print("---------------------------------------") --séparation sur la page html
end

client.subscribe("MASTER",mqtt.QOS0, Temperature)