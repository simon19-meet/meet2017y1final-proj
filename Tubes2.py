import turtle
import random

size_x = 800
size_y = 500
square_size = 20
start_y_pos = 100
TIME_STEP = 100
tube_list = []
counter = 0
counter2 = 0
#tube = turtle.clone()

turtle.tracer(1,0)
turtle.setup(size_x,size_y)
#turtle.hideturtle()

#start_y_pos = random.randint(0,size_y/2)

#turtle.shape("square")
#Generate stamps by turtle positions to make the tubes
#random length 1-10
##LEFT="Left"
##LEFT_D=1
##direction=LEFT_D

def create_tube():
##    random_y_pos = random.randint(0,size_y/2)
##    tube.goto(size_x/2,random_y_pos)
##    tube_list.append(tube)
##    tube2=turtle.clone()
##    tube2.penup()
##    tube2.shape('square')
##    random_y_pos = random.randint(0,size_y/2-150)
##    tube2.goto(size_x/2,random_y_pos)
##    tube_list.append(tube2)
##    if abs( - )
    # tube object creation
    tube = turtle.clone()
    tube.penup()
    tube.shape('square')
    tube2=turtle.clone()
    tube2.penup()
    tube2.shape('square')
    # getting valid random tube positions
    tube1_y = random.randint(0,size_y/2)
    tube2_y = random.randint(0,size_y/2)
    while abs(tube1_y - tube2_y) < 3 * square_size:
        tube1_y = random.randint(0,size_y/2)
        tube2_y = random.randint(0,size_y/2)
    tube.goto(size_x/2,tube1_y)
    tube2.goto(size_x/2,tube2_y)
    tube_list.append(tube)
    tube_list.append(tube2)
    

def move_tubes():
    global counter,counter2
    for tube in tube_list:
        my_pos = tube.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        if x_pos < -size_x/2:
            tube_list.remove(tube)
        
        tube.goto(x_pos - square_size,y_pos)

    counter += 1
    if counter%10 == 0:
        create_tube()

    turtle.ontimer(move_tubes,TIME_STEP)
##    for tube2 in tube_list:
##        my_pos_2 = tube2.pos()
##        x_pos_2 = my_pos_2[0]
##        y_pos_2 = my_pos_2[1]
##        if x_pos_2 < -size_x/2:
##            tube_list.remove(tube2)
##        
##        tube2.goto(x_pos_2 - square_size,y_pos_2)
##    counter2 += 1
##    if counter2%10 == 0:
##        create_tube()

create_tube()
move_tubes()

##    global direction
##    direction=LEFT_D
####turtle.pu()
####turtle.goto(300,100)
####turtle.stamp()
####turtle.rt(90)
####turtle.fd(100)
####turtle.stamp()
##    turtle.setheading(90)
##    turtle.heading()
##    
###turtle.onkeypress(move_tubes,)
###turtle.listen()
##    turtle.ontimer(move_tubes,100)
##move_tubes()


##tube1=turtle.clone()
##turtle.register_shape("tube1.gif")
##tube1.shape("tube1.gif")

