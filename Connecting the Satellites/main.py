import time
import random
import pgzrun

HEIGHT=500
WIDTH=600

TITLE="Connecting the Satellites"

num_of_sat = 8
start_time=0
end_time=0
total_time=0

sats = []

for i in range(0,num_of_sat):
    satellite = Actor("satellite")
    satellite.x=random.randint(50,WIDTH-100)
    satellite.y=random.randint(50,HEIGHT-100)
    sats.append(satellite)
start_time=time.time()


def draw():
    screen.blit("space",(0,0))
    number=1
    for i in sats:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number+=1
    screen.draw.text(str(round(start_time,1)),(10,10))

def update():
    pass

pgzrun.go()