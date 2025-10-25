import time
import random
import pgzrun

HEIGHT = 500
WIDTH = 600
TITLE = "Connecting the Satellites"

num_of_sat = 8
next_sat = 0
start_time = 0
game_over = False
you_won = False
game_duration = 10.0

sats = []
lines = []

for i in range(0, num_of_sat):
    satellite = Actor("satellite")
    satellite.x = random.randint(50, WIDTH - 100)
    satellite.y = random.randint(50, HEIGHT - 100)
    sats.append(satellite)

start_time = time.time()

def draw():
    global game_over, start_time, you_won

    screen.blit("space", (0, 0))

    # --- check time limit ---
    if not game_over and not you_won:
        if time.time() - start_time >= game_duration:
            game_over = True

    # --- draw satellites and lines ---
    number = 1
    for i in sats:
        screen.draw.text(str(number), (i.pos[0], i.pos[1] + 20))
        i.draw()
        number += 1

    for i in lines:
        screen.draw.line(i[0], i[1], "white")

    # --- timer display ---
    if not game_over and not you_won:
        time_left = game_duration - (time.time() - start_time)
        screen.draw.text(f"Time Left: {round(time_left, 1)}", (10, 10), color="yellow")

    # --- winning condition ---
    if you_won:
        total_time = time.time() - start_time
        screen.fill("black")
        screen.draw.text(f"You Won!",color="green",center=(WIDTH / 2, HEIGHT / 2))

    # --- game over condition ---
    elif game_over:
        screen.fill("black")
        screen.draw.text(
            "Game Over!\nYour Time Is Up!",
            color="red",
            center=(WIDTH / 2, HEIGHT / 2))


def update():
    pass


def on_mouse_down(pos):
    global next_sat, lines, game_over, you_won
    if not game_over and not you_won:
        if next_sat < num_of_sat:
            if sats[next_sat].collidepoint(pos):
                if next_sat:
                    lines.append((sats[next_sat - 1].pos, sats[next_sat].pos))
                next_sat += 1

                # ✅ player connected all satellites in time
                if next_sat == num_of_sat:
                    you_won = True

pgzrun.go()
