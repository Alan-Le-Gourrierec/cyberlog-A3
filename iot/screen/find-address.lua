try(
    function ()
        i2c.setpin(1,18,19)
        screen = i2c.attach(i2c.I2C1,i2c.MASTER)
    end,function ()end, function ()end
)

function catch(what)
    return what[1]
end

function test(what)
    s,r = pcall(what)
    if not s then
        what[3](r)
    else what[1]()
    end
    return r
end

for i=0,127 do
    try(
        function ()
            print(string.format("trouvé #%x",i))
        end,

        function ()
            screen:start()
            screen:address(i,false)
            screen:stop()
        end,

        catch(
            function (error)
        end
        )
   )
end