try(
    function ()
            s = servo.attach(pio.GPIO23)
    end
)

s:write(90)