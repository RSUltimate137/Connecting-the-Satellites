import time
import random
import pgzrun

HEIGHT=500
WIDTH=600

TITLE="Connecting the Satellites"

num_of_sat = 8
next_sat = 0
start_time=0
game_over = False
game_duration = 10.0

sats = []
lines = []

for i in range(0,num_of_sat):
    satellite = Actor("satellite")
    satellite.x=random.randint(50,WIDTH-100)
    satellite.y=random.randint(50,HEIGHT-100)
    sats.append(satellite)
start_time=time.time()

def draw():
    global game_over, start_time

    if time.time() - start_time >= game_duration:
        game_over = True

    screen.blit("space",(0,0))
    number=1
    for i in sats:
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        i.draw()
        number+=1
    for i in lines:
        screen.draw.line(i[0],i[1],("white"))
    
    if not game_over:
        time_left = game_duration - (time.time() - start_time)
        screen.draw.text(f"Time Left: {round(time_left, 1)}",(10,10),color="yellow")

    else:
        screen.fill("black")
        screen.draw.text("Game Over!\n Your Time Is Up!", color="red", center=(WIDTH/2,HEIGHT/2))
    
    # if next_sat < num_of_sat:
    #     total_time = time.time()-start_time
    #     screen.draw.text(str(round(total_time,1)),(10,10))
    # else:
    #     screen.draw.text(str(round(total_time,1)),(10,10))

def update():
    pass

def on_mouse_down(pos):
    global next_sat,lines,game_over
    if not game_over:
        if next_sat < num_of_sat:
            if sats[next_sat].collidepoint(pos):
                if next_sat:
                    lines.append((sats[next_sat-1].pos,sats[next_sat].pos))
                next_sat = next_sat+1

                if next_sat == num_of_sat:
                     game_over = True
        else:
            lines = []
            next_sat = 0

pgzrun.go()