try(
    function ()
        i2c.setpins(1,18,19)
        screen = i2c.attach(i2c.I2C1,i2c.MASTER)
    end,
    function (where,line,error,message)
        print(message)
    end, function ()end
)

function found()
        for i=0,127 do
        try(
            function ()
                screen:start()
                screen:address(i,false)
                screen:stop()
                print(string.format("trouve # %x",i))
            end,
            function (where,error,line,message)
            end
        )
    end
end