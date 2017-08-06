import turtle

turtle.shape("square")
#Generate stamps by turtle positions to make the tubes
#random length 1-10
turtle.pu()
turtle.goto(300,200)
turtle.rt(90)
for i in range(1,5):
    turtle.stamp()
    turtle.fd(20)
turtle.forward(60)
for x in range(1,5):
    turtle.stamp()
    turtle.fd(20)

