from sense_hat import SenseHat
import pygame
import numpy as np
import random
import os

# This is a list with all sounds the robot will make
sounds = ["/home/pi/microbe_obliterator/sounds/romo{:}.mp3".format(x) for x in range(1, 8)]

# Use the sense hat for the IMU, and use pygame for playing sounds
sense = SenseHat()
pygame.mixer.init()


maxred = 10
maxgreen = 10
maxblue = 10
while True:
    r = int(maxred)
    g = int(maxgreen)
    b = int(maxblue)

    # If the robot is not playing music and having a red pattern, create the thinking pattern
    # Set random red, green and blue pixels and shift the RGB ranges a bit. 
    if not pygame.mixer.music.get_busy():
        for i in range(20):
            sense.set_pixel(random.randint(0, 7), random.randint(0,7), random.randint(0,r), random.randint(0, g), random.randint(0, b))
        maxred = (maxred+1)%255
        maxgreen = (maxgreen+2)%255
        maxblue = (maxblue+3)%255


    # Get the acceleration from the IMU on the python sense hat
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    print("{:3.3f}".format(x))


    # If there is a large positive movement in the x direction
    if x > 0.322:
        # Play a sound if the robot is not already playing music
        if not pygame.mixer.music.get_busy():
            # Set 50 random pixels to a random red value
            for i in range(50):
                sense.set_pixel(random.randint(0,7), random.randint(0,7), random.randint(100,255), random.randint(0, 50), random.randint(0,0))
            pygame.mixer.music.load(random.choice(sounds))
            pygame.mixer.music.play()
    
