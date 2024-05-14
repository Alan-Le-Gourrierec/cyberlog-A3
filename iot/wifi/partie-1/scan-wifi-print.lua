try(
    function ()
        w = net.wf.scan(true)
    end,
    function (message)
        print(message)
    end
)

function scan_wifi()
    condition = true
    i = 0
    while condition == true do
       try(function ()
            if w[i].auth == 0 then
                console(w[i].ssid.."  "..w[i].rssi)
            end
            i = i + 1
       end,
       function ()
            condition = false
       end
    )
    end
end
