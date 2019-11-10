import turtle
window=turtle.Screen()
window.bgcolor("#000000")
window.title("Farnam's Pen Code")
turtle_pen=turtle.Pen()
turtle_pen.pencolor("#ffffff")
turtle_pen.speed(0)
for counter in range(1000):
    turtle_pen.forward(100)
    turtle_pen.right(45)
    turtle_pen.forward(40)
    turtle_pen.backward(700)
    turtle_pen.left(.5)