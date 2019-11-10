import turtle
window=turtle.Screen()
window.bgcolor("#11ff00")
window.title("Farnam's Pen Code")
turtle_pen=turtle.Pen()
turtle_pen.pencolor("#1500ff")
turtle_pen.speed(0)
for counter in range(1000):
    turtle_pen.forward(counter)
    turtle_pen.left(115655)