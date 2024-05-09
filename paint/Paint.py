from turtle import *
from freegames import vector

def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
    up()

def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(4):
        forward(end.x - start.x)
        left(90)
    end_fill()
    up()

def draw_circle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    radius = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5 / 2
    circle(radius)
    end_fill()
    up()

def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()
    up()

def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()
    up()

def tap(x, y):
    state['start'] = vector(x, y)

def drag(x, y):
    end = vector(x, y)
    shape = state['shape']
    start = state['start']
    if start is not None:
        shape(start, end)
        state['start'] = end
        update()

def store(key, value):
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
ondrag(drag)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'k')
onkey(lambda: color('white'), 'w')
onkey(lambda: color('green'), 'g')
onkey(lambda: color('blue'), 'b')
onkey(lambda: color('red'), 'r')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
tracer(False)  #  las actualizaciones automáticas de la pantalla
done()
