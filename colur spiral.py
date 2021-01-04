import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
  
while (True):  
    for i in range(6):  
        for colors in ["red", "blue", "magenta", "green", "yellow", "white", "cyan"]:  
            turtle.color(colors)  
            turtle.circle(150)  
            turtle.left(10)  
  
  
turtle.hideturtle()  
turtle.mainloop()  
