import turtle #importing library
loadWindow = turtle.Screen()
turtle.speed(2) #speed of turtle
 
for i in range(100): #iterate for loop
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()
