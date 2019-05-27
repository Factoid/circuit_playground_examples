from adafruit_circuitplayground.express import cpx
import time
import adafruit_fancyled.adafruit_fancyled as fancy
import math

hue = 0
color = (255,0,0)
print("Starting")
cpx.pixels.fill(0)
cpx.pixels.show()
cpx.pixels.brightness = 0.1
minBrightness =0.01
maxBrightness =0.5
rampUp = True
valMax = -10000
valMin = 10000
while True:
    x,y,z = cpx.acceleration
    if cpx.button_b:
        if rampUp:
            cpx.pixels.brightness += 0.02
            if( cpx.pixels.brightness >= maxBrightness ):
                cpx.pixels.brightness = maxBrightness
                rampUp = False
        else:
            cpx.pixels.brightness -= 0.02
            if cpx.pixels.brightness <= minBrightness:
                cpx.pixels.brightness = minBrightness
                rampUp = True
    if cpx.switch:
        val = math.atan2(y,x)
        hue = (val + 3.14159)/(2*3.14159)
        color = fancy.CHSV(hue,255,255)
        # converts float HSV values to integer RGB values
        packed = color.pack()
        # writes converted int values to NeoPixels
        cpx.pixels.fill(packed);
    time.sleep(0.1)
