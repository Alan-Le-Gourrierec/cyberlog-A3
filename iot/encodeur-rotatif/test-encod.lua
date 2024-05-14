function Lecture(dir,counter,button)
    print("direction:"..dir..",counter:"..counter..",button:"..button)
end

encod = encoder.attach(pio.GPIO19,pio.GPIO21,pio.GPIO5,Lecture)

while true do 
    try(
    function () -- try to be done
        p,s =encod:read()
        print(p,s)
    end,
    function (where,line,error,message) --do if error
        print(message)
    end,
    function () --do each time   
    end
    )
end