# James Jack
# 2/13/21
# program draws spiral shape and fills color in it

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
james = turtle.Turtle()
james.color("red")
james.shape("classic")

james.fillcolor("green")
james.begin_fill()
for size in range(10, 80, 2):
    james.forward(size)
    james.right(30)
james.end_fill()

wn.exitonclick()
