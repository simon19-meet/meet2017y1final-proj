import turtle

turtle.shape("square")
#Generate stamps by turtle positions to make the tubes
#random length 1-10
LEFT="Left"
LEFT_D=1
direction=LEFT_D
def move_tubes():
    global direction
    direction=LEFT_D
##turtle.pu()
##turtle.goto(300,100)
##turtle.stamp()
##turtle.rt(90)
##turtle.fd(100)
##turtle.stamp()
    turtle.setheading(90)
    turtle.heading()
    
#turtle.onkeypress(move_tubes,)
#turtle.listen()
    turtle.ontimer(move_tubes,100)
move_tubes()


##tube1=turtle.clone()
##turtle.register_shape("tube1.gif")
##tube1.shape("tube1.gif")

