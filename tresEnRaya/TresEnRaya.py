from turtle import *
import tkinter as tk
from tkinter import messagebox

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8, 'board': [[] for _ in range(8)]}

def line(x_start, y_start, x_end, y_end):
    "Draw line from (x_start, y_start) to (x_end, y_end)."
    up()
    goto(x_start, y_start)
    down()
    goto(x_end, y_end)
    up()

def grid():
    bgcolor('light blue')
    for x in range(-150, 200, 50):
        line(x, -200, x, 200)
    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')
    update()

def tap(x, y):
    row = int((x + 200) // 50)
    col = state['rows'][row]
    player = state['player']

    if col < 8:
        x = row * 50 - 175
        y = col * 50 - 175
        up()
        goto(x, y)
        dot(40, player)
        update()

        state['board'][row].append(player)
        state['rows'][row] = col + 1

        if check_win(row, col, player):
            messagebox.showinfo("Game Over", f"{player} ha ganado!")
            onscreenclick(None)
        else:
            state['player'] = turns[player]

def check_win(row, col, player):
    directions = [
        (1, 0),  # Horizontal
        (0, 1),  # Vertical
        (1, 1),  # Diagonal /
        (1, -1)  # Diagonal \
    ]
    for dx, dy in directions:
        count = 1
        for d in [1, -1]:
            n = 1
            while True:
                r = row + n * dx * d
                c = col + n * dy * d
                if 0 <= r < 8 and 0 <= c < len(state['board'][r]) and state['board'][r][c] == player:
                    count += 1
                    n += 1
                else:
                    break
        if count >= 4:
            return True
    return False

def main():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    onscreenclick(tap)
    done()

main()
