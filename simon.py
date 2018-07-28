from adafruit_circuitplayground.express import cpx
import time
import random

def light_blue():
    cpx.pixels[0] = (0,0,255)
    cpx.pixels[1] = (0,0,255)
    cpx.pixels[2] = (0,0,255)
    
def blue():
    cpx.pixels.fill((0,0,0))
    light_blue()
    cpx.pixels.show()
    if cpx.switch:
        cpx.play_tone(329.628,0.5)
    else:
        time.sleep(0.5)

def light_green():
    cpx.pixels[5] = (0,255,0)
    cpx.pixels[6] = (0,255,0)
    cpx.pixels[7] = (0,255,0)
    
def green():
    cpx.pixels.fill((0,0,0))
    light_green()
    cpx.pixels.show()
    if cpx.switch:
        cpx.play_tone(164.814,0.5)
    else:
        time.sleep(0.5)
        
def light_yellow():
    cpx.pixels[7] = (255,255,0)
    cpx.pixels[8] = (255,255,0)
    cpx.pixels[9] = (255,255,0)
    
def yellow():
    cpx.pixels.fill((0,0,0))
    light_yellow()
    cpx.pixels.show()
    if cpx.switch:
        cpx.play_tone(277.183,0.5)
    else:
        time.sleep(0.5)

def light_red():
    cpx.pixels[2] = (255,0,0)
    cpx.pixels[3] = (255,0,0)
    cpx.pixels[4] = (255,0,0)

def red_hint():
    light_red()
    random.choice([light_blue,light_yellow])()

def green_hint():
    light_green()
    random.choice([light_red,light_blue])()

def blue_hint():
    light_blue()
    random.choice([light_green,light_yellow])()
    
def yellow_hint():
    light_yellow()
    random.choice([light_red,light_blue])()

def red():
    cpx.pixels.fill((0,0,0))
    light_red()
    cpx.pixels.show()
    if cpx.switch:
        cpx.play_tone(440.0,0.5)
    else:
        time.sleep(0.5)
        
def win_round():
    for i in range(11):
        t = i/10.0
        cpx.stop_tone()
        if cpx.switch:
            cpx.start_tone( 220.0 * (1.0-t) + 440.0 * t )
        cpx.pixels.fill((0,32,0))
        for j in range(0,10,2):
            cpx.pixels[j] = (0,255,0)
        cpx.pixels.show()
        cpx.pixels.fill((0,32,0))
        for j in range(1,10,2):
            cpx.pixels[j] = (0,255,0)
        cpx.pixels.show()
    cpx.pixels.fill(0)
    cpx.pixels.show()
    cpx.stop_tone()
    time.sleep(0.25)
    
def lose_round():
    for i in range(10):
        cpx.stop_tone()
        if cpx.switch:
            cpx.start_tone( [220.0,190.0][i%2] )
        cpx.pixels.fill((32,0,0))
        for j in range(0,10,2):
            cpx.pixels[j] = (255,0,0)
        cpx.pixels.show()
        cpx.pixels.fill((32,0,0))
        for j in range(1,10,2):
            cpx.pixels[j] = (255,0,0)
        cpx.pixels.show()
    cpx.pixels.fill(0)
    cpx.pixels.show()
    cpx.stop_tone()
    time.sleep(0.25)
    
funcs = [(blue,blue_hint),(green,green_hint),(red,red_hint),(yellow,yellow_hint)]

cpx.pixels.brightness = 0.1
sequence = []
sequence.append(random.choice(funcs))
sequence.append(random.choice(funcs))
cpx.adjust_touch_threshold(20)
while True:
    for c in sequence:
        c[0]()
    
    i = 0
    hint = False
    while i < len(sequence):
        cpx.pixels.fill((0,0,0))
        cpx.pixels.show()
        guess = None
        if cpx.button_a and not hint:
            hint = True
            sequence[i][1]()
            cpx.pixels.show()
            time.sleep(0.5)
        elif cpx.touch_A1:
            guess = green
        elif cpx.touch_A3 or cpx.touch_A2:
            guess = yellow
        elif cpx.touch_A4 or cpx.touch_A5:
            guess = blue
        elif cpx.touch_A7 or cpx.touch_A6:
            guess = red
        
        if guess != None:
            if sequence[i][0] == guess:
                i += 1
                guess()
            else:
                i = -1
                break
  

    if i == len(sequence):
        win_round()
        sequence.append(random.choice(funcs))
    elif i == -1:
        lose_round()
        sequence = []
        sequence.append(random.choice(funcs))
        sequence.append(random.choice(funcs))