import turtle 

turtle.bgcolor('black')
turtle.speed('80')
turtle.hideturtle()

colors = ["blue", "purple", "blue", "purple"]

for i in range(120):
  for c in colors:
    turtle.colors(c)
    turtle.circle(200-i, 100)
    turtle.lt(90)
    turtle.circle(200-i, 100)
    turtle.end_fill()

turtle.mainloop()