import turtle
import time
import pygame
import random

turtle.tracer(2,0)

size_x = 800
size_y = 500
turtle.setup(size_x, size_y)
square_size = 20
start_y_pos = 100
TIME_STEP = 100
tube_list = []
tube_pos = []
counter = 0
counter2 = 0
food_list=['chocolate.gif','fries.gif','ham.gif','pizzzzza.gif','icee.gif']
SIZE_X=1200
SIZE_Y=900
turtle.setup(SIZE_X,SIZE_Y)
turtle.bgcolor("light blue")


tube_pos_top = []
tube_pos_bottom = []

def create_tube():
    global tube_list, tube_pos_top, tube_pos_bottom
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
    
    ########################### NEW CODE ######################################
    #tube1 is the upper tube, tube2 is the lower tube
    if tube2_y > tube1_y:
        temp = tube1_y
        tube1_y = tube2_y
        tube2_y = temp

    tube.goto(size_x/2,tube1_y)
    tube2.goto(size_x/2,tube2_y)

    temp = []
    temp.append(tube)
    temp.append(tube2)

    tube_list.append(temp)
    
    tube_pos_top.append(tube.pos())
    tube_pos_bottom.append(tube2.pos())
    
    tube_pos.append(tube.pos())
    tube_pos.append(tube2.pos())
    ##############################################################################
##    turtle.ontimer(create_tube, 1000)

def move_tubes():
    ############## ALL OF MOVE_TUBES IS NEW ##################################
    global counter, tube_list, tube_pos_top, tube_pos_bottom

    for i in range(len(tube_list)):
        try:
            print(i)
            this_top_tube = tube_list[i][0]
            this_bottom_tube = tube_list[i][1]

            if (this_top_tube.pos()[0] < -size_x/2) or (this_bottom_tube.pos()[0] < -size_x/2):
                tube_list.pop(i)
                tube_pos_top.pop(i)
                tube_pos_bottom.pop(i)

            else:
                this_top_tube.goto(this_top_tube.pos()[0] - square_size,this_top_tube.pos()[1])
                tube_pos_top[i] = this_top_tube.pos()

                this_bottom_tube.goto(this_bottom_tube.pos()[0] - square_size,this_bottom_tube.pos()[1])
                tube_pos_bottom[i] = this_bottom_tube.pos()

                food_clone = tube_list[i][2]
                food_clone_pos = food_clone.pos()
                food_clone.goto(food_clone.pos()[0] - square_size, food_clone.pos()[1])


        except IndexError:
            pass
    
    counter += 1
    if counter%20 == 0:
        create_tube()
##    create_tube()

##    turtle.ontimer(move_tubes,TIME_STEP)


create_tube()
##move_tubes()

def create_food():
    tube = turtle.clone()
    tube.penup()
    tube.shape('square')
    tube2=turtle.clone()
    tube2.penup()
    tube2.shape('square')
    
    
##    turtle.register_shape('chocolate.gif')
##    turtle.register_shape('fries.gif')
##    turtle.register_shape('ham.gif')
##    turtle.register_shape('pizzzzza.gif')
##    turtle.register_shape('icee.gif')
##    chocolate=turtle.clone()
##    chocolate.shape('chocolate.gif')
##    fries=turtle.clone()
##    fries.shape('fries.gif')
##    ham=turtle.clone()
##    ham.shape('ham.gif')
##    pizzzzza=turtle.clone()
##    pizzzzza.shape('pizzzzza.gif')
##    icee=turtle.clone()
##    icee.shape('icee.gif')

    
create_food()
##def move_food():
##    global counter2, tube_list
##    for chocolate in food_list:
##        my_pos_2 = chocolate.pos()
##        x_pos = my_pos_2[0]
##        y_pos = my_pos_2[1]
##        
##move_food()


pygame.mixer.init()

pygame.mixer.music.load("ibelive.mp3")

pygame.mixer.music.play(-1)


timing = 0
turtle.setup(size_x,size_y)
##turtle.hideturtle()
turtle.register_shape("newnewnew_bird.gif")
turtle.register_shape("poof.gif")

writer = turtle.clone()
writer.hideturtle()
writer.penup()
writer.goto(200, 250)
##writer.write("This way to Kenya -->", font=("Arial", 24, "normal"))
##writer.goto(200, 210)
##writer.write("get there to give the", font=("Arial", 24, "normal"))
##writer.goto(200, 170)
##writer.write("children food!", font=("Arial", 24, "normal"))
##writer.goto(-530, 250)
#writer.write("You'll get to Kenya in: ", font=("Arial", 24, "normal"))

birdy = turtle.clone()
birdy.shape("newnewnew_bird.gif")
birdy.penup()
birdy.showturtle()

score = turtle.clone()
score.penup()
score.hideturtle()
score.goto(-210, 250)

UP_ARROW = "Up"
LEFT_ARROW = "Left"

draw = turtle.clone()
draw.hideturtle()
def times():
    global time
    timing += 1

def distance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    return d

def grav():
    global timing
    my_pos = birdy.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    birdy.goto(x_pos, (y_pos - 10))

    if birdy.pos()[1] > 360:
        draw.write("GAME OVER! :(", font=("Arial", 30, "normal"),align="center")
        pygame.mixer.init()
        pygame.mixer.music.load("hello_darkness.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        quit()
    if birdy.pos()[1] < -360:
        draw.write("GAME OVER! :(", font=("Arial", 30, "normal"),align="center")
        pygame.mixer.init()
        pygame.mixer.music.load("hello_darkness.mp3")
        pygame.mixer.music.play()
        time.sleep(10)
        quit()
    timing += 1
    score.clear()
    #score.write(str(10000 - timing), font=("Arial", 24, "normal"))
    if timing == 10000:
        draw.write("You won!", font=("Ariel", 30, "normal"),align="center")
        time.sleep(3)
##    if birdy.pos() in tube_pos:
##        quit()
    for tube in tube_list:
        d_top = distance(tube[0].pos(),birdy.pos())
        d_bottom = distance(tube[1].pos(),birdy.pos())
        print(d_top, d_bottom)
        if (d_top < 20) or (d_bottom < 20):
            pygame.mixer.init()
            pygame.mixer.music.load("hello_darkness.mp3")
            pygame.mixer.music.play()
            time.sleep(10)
            quit()
    

    ############ kat's code ################
    for i in range(len(tube_list)):
        #print('TOP: ',tube_pos_top[i])
        if abs(x_pos - tube_pos_top[i][0]) < 20:
            if (y_pos > tube_pos_top[i][1]) or (y_pos < tube_pos_bottom[i][1]):
                print('ABOVE OR BELOW A TUBE')
                time.sleep(2)
                quit()

    #########################################
    move_tubes()
    turtle.ontimer(grav, 50)
    
def red():
    turtle.bgcolor("red")
turtle.onkeypress(red, LEFT_ARROW)

grav()

def up():
##    move_tubes()
    for i in range(7):
        my_pos = birdy.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        birdy.goto(x_pos, y_pos + 10)
    
turtle.onkeypress(up, UP_ARROW)
turtle.listen()


turtle.mainloop()

##global food_stamp,food_pos
##if birdy.pos() in food_pos:
##    global score
##    food_ind=food_pos.index(birdy.pos())
##    food.clearstamp(food_stamp[food_ind])
##    food_stamp.pop(food_ind)
##    food_pos.pop(food_ind)
##    score+=1
##    scorePen = turtle.clone()
##    scorePen.color("light blue")
##    scorePen.shape("square")
##    scorePen.hideturtle()
##    scorePen.penup()
##    scorePen.goto(230, 192)
##    scorePen.stamp()
##    scorePen.goto(230 + SQUARE_SIZE, 192)
##    scorePen.stamp()
##    scorePen.goto(125,175)
##    scorePen.color("black")
##    scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
##    print("you have eaten the food and scored one point!!!")
##    scorePen.color("white")
##    scorePen.circle(30)
##    make_food()

