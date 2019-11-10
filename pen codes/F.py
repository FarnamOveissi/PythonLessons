import turtle
window=turtle.Screen()
window.bgcolor("#11ff00")
window.title("Farnam's Pen Code")
turtle_pen=turtle.Pen()
turtle_pen.pencolor("#1500ff")
for counter in range(7):
    turtle_pen.forward(25)
    turtle_pen.left(90)
    turtle_pen.forward(60)
    turtle_pen.right(90)
    turtle_pen.forward(40)
    turtle_pen.left(90)
    turtle_pen.forward(25)
    turtle_pen.left(90)
    turtle_pen.forward(40)
    turtle_pen.right(90)
    turtle_pen.forward(35)
    turtle_pen.right(90)
    turtle_pen.forward(55)
    turtle_pen.left(90)
    turtle_pen.forward(25)
    turtle_pen.left(90)
    turtle_pen.forward(80)
    turtle_pen.left(90)
    turtle_pen.forward(145)
    turtle_pen.left(90)
    if counter>-1:
        turtle_pen.pencolor("#11ff00")
    if counter>0:
        turtle_pen.pencolor("#ff00bb")
    if counter>1:
        turtle_pen.pencolor("#11ff00")
    if counter>2:
        turtle_pen.pencolor("#00f2ff")
    if counter>3:
        turtle_pen.pencolor("#11ff00")
    if counter>4:
        turtle_pen.pencolor("#ff0000")