import time
import random
import pgzrun

HEIGHT=500
WIDTH=600

TITLE="Connecting the Satellites"

num_of_sat = 8

sats = []

for i in range(0,num_of_sat):
    satellite = Actor("satellite")
    satellite.x=random.randint(50,WIDTH-100)
    satellite.y=random.randint(50,HEIGHT-100)

    sats.append(satellite)


def draw():
    for i in sats:
        print(i)

def update():
    pass

pgzrun.go()