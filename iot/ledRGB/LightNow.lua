-- permet de ne pas reboot à chaque fois que nous lanceons une fonction ou plus précisément
-- d'essayer si ceci n'as pas encore été fait
try(
    function ()
        r = pwm.attach(pio.GPIO18,4,0.1)
    end,function ()end,function ()end
)
try(
    function ()
        v = pwm.attach(pio.GPIO19,4,0.1)
    end,function ()end,function ()end
)
try(
    function ()
        b = pwm.attach(pio.GPIO21,4,0.1)
    end,function ()end,function ()end
)

function rvb(r2,v2,b2)
    r:setduty(r2//255)
    v:setduty(v2/255)
    b:setduty(b2//255)
end
-- ceci est le même mode de fonctionnement pour l'alumage progressif de la led
r:start();v:start();b:start()

for i=0,255 do rvb(i,0,0);tmr.delayms(20) end
for i=0,255 do rvb(i,i,0);tmr.delayms(20) end
for i=0,255 do rvb(0,i,0);tmr.delayms(20) end
for i=0,255 do rvb(0,i,i);tmr.delayms(20) end
for i=0,255 do rvb(0,0,i);tmr.delayms(20) end
for i=0,255 do rvb(i,0,i);tmr.delayms(20) end

r:stop();r:detach()
v:stop();v:detach()
b:stop();v:detach()
