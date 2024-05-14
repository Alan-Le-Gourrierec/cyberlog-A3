--creation du reseau wifi
try(
    function ()
        net.wf.setup(net.wf.mode.AP,"AlanTest","chinatown")
    end,
    function (message)print(message.." reseau")end
)

function StartAlan()
    net.wf.start()
    net.wf.http.start()
    nb = 0 -- la variable global qui permet de faire le compteur sur le mini serveur html
end

function DownAlan()
    net.wf.stop()
end