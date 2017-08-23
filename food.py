import turtle
import random

size_x=800
size_y=500
turtle.setup(size_x,size_y)
square_size=20
start_y_pos = 100
TIME_STEP = 100
tube_list = []
tube_pos = []
counter = 0
counter2 = 0

def create_food():
    tube = turtle.clone()
    tube.penup()
    tube.shape('square')
    tube2=turtle.clone()
    tube2.penup()
    tube2.shape('square')
    
    turtle.register_shape('chocolate.gif')
    turtle.register_shape('fries.gif')
    turtle.register_shape('ham.gif')
    turtle.register_shape('pizzzzza.gif')
    turtle.register_shape('icee.gif')
    chocolate=turtle.clone()
    chocolate.shape('chocolate.gif')
    fries=turtle.clone()
    fries.shape('fries.gif')
    ham=turtle.clone()
    ham.shape('ham.gif')
    pizzzzza=turtle.clone()
    pizzzzza.shape('pizzzzza.gif')
    icee=turtle.clone()
    icee.shape('icee.gif')

    food_list=['chocolate.gif','fries.gif','ham.gif','pizzzzza.gif','icee.gif']
    end_range = len(food_list)
    food_ind = random.randint(0,end_range)
##    addimage(food_list[food_ind])
    tube1_y = random.randint(0,size_y/2)
    tube2_y = random.randint(0,size_y/2)
    while abs(tube1_y - tube2_y) < 3 * square_size:
        tube1_y = random.randint(0,size_y/2)
        tube2_y = random.randint(0,size_y/2)
    tube.goto(size_x/2,tube1_y)
    tube2.goto(size_x/2,tube2_y)
    tube_list.append(tube)
    tube_list.append(tube2)
    tube_pos.append(tube.pos())
    tube_pos.append(tube2.pos())
create_food()
move_tubes()
def move_tubes():
    global counter,counter2, tube_list
    for tube in tube_list:
        my_pos = tube.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        if x_pos < -size_x/2:
            tube_list.remove(tube)
        
        tube.goto(x_pos - square_size,y_pos)

    counter += 1
    if counter%20 == 0:
        create_tube()

