import turtle
window=turtle.Screen()
window.bgcolor("#11ff00")
window.title("Farnam's Pen Code")
turtle_pen=turtle.Pen()
turtle_pen.pencolor("#1500ff")
turtle_pen.speed(0)
for counter in range(1000):
    turtle_pen.forward(counter)
    turtle_pen.left(20)
    if counter>15:
        turtle_pen.pencolor("#ff00f7")
    if counter>30:
        turtle_pen.pencolor("#ff0080")
    if counter>45:
        turtle_pen.pencolor("#ff0044")
    if counter>50:
        turtle_pen.pencolor("#8f0000")
        turtle_pen.forward(counter)
        turtle_pen.backward(counter)
        turtle_pen.left(1451451450)