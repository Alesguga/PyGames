from random import randrange
from turtle import *
from freegames import square, vector
import tkinter as tk
from tkinter import messagebox

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        game_over()
        return

    snake.append(head)

    if head == food:
        print('snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

def game_over():
    answer = tk.messagebox.askretrycancel("Game Over", "Otra vez?")
    if answer:
        reset()
    else:
        bye()

def reset():
    global snake, food, aim
    snake = [vector(10, 0)]
    food = vector(0, 0)
    aim = vector(0, -10)
    clear()
    move()

def main():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()

main()
