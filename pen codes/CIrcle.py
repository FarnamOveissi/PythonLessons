import turtle
window=turtle.Screen()
window.bgcolor("#11ff00")
window.title("Farnam's Pen Code")
turtle_pen=turtle.Pen()
turtle_pen.pencolor("#1500ff")
turtle_pen.pensize(1)
turtle_pen.speed(0)
for counter in range(1000):
    turtle_pen.forward(1)
    turtle_pen.left(1)
    if counter>360:
        turtle_pen.pencolor("#fc0303")
        turtle_pen.forward(counter)
        turtle_pen.backward(counter)
        turtle_pen.left(145)