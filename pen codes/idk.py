import turtle
window=turtle.Screen()
window.bgcolor("#ffffff")
window.title("Farnam's Pen Code")
turtle_pen=turtle.Pen()
turtle_pen.pencolor("#000000")
turtle_pen.speed(0)
for e in range(1000):
    turtle_pen.forward(e)
    turtle_pen.left(91)