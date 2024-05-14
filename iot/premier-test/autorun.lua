pio.pin.setdir(pio.OUTPUT,pio.GPIO2)
dofile("blink.lua")

print("Hello !")
blink(5)
print("are you alright ?")
