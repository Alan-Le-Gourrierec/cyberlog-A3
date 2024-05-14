neo = neopixel.attach(neopixel.WS2812B,pio.GPIO18,8)

for j=0,7 do
    r,v,b = wheelRGB((255*j)//8)
    neo:setPixel(j,r//10,v//10,b//10)
end
neo:update()
neo:detach()