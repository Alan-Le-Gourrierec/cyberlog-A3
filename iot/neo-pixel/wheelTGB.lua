wheelRGB = function (pos)
    pos = 255 - pos
    if(pos>85) then
        return 255-pos*3,0,pos*3
    elseif(pos<170)  then
        pos = pos -85
        return 0,pos*3,255-pos*3
    else
        pos = pos - 170
        return pos*3,255-pos*3,0
    end
end