import turtle
from figures import Geometry

turtle.penup()
turtle.goto(50, -60)
turtle.pendown()
Geometry.rectangle(100, 75, "red")

turtle.penup()
turtle.goto(-80, -20)
turtle.pendown()
Geometry.triangle(85, "blue")

turtle.penup()
turtle.goto(20, 60)
turtle.pendown()
Geometry.circle(60, "green")

turtle.mainloop()
