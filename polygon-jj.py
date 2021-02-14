# James Jack
# 2/13/21
# program draws polygon based on user input


import turtle  # loads graphics program

wn = turtle.Screen()  # creates screen
james = turtle.Turtle()  # names turtle

sides = int(input("how many sides?"))
length = int(input("how long is the side?"))
color = input("what color are the lines?")
fillcolor = input("what color is it filled with?")

james.color(color)  # command to color lines selection
james.fillcolor(fillcolor)  # command for fill color selection

james.begin_fill()  # command to begin fill
for i in range(sides):  # range command to loop drawing of sides
    james.forward(length)  # command to draw specified length
    james.left(360 / sides)  # command to create angles based on the sides given
james.end_fill()   # end fill

wn.exitonclick()   # exit the window from click
