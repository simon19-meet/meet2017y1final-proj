import turtle
import time
turtle.hideturtle()
turtle.register_shape("newnew_bird.gif")

birdy = turtle.clone()
birdy.shape("newnew_bird.gif")
birdy.penup()
birdy.showturtle()

UP_ARROW = "Up"

draw = turtle.clone()
draw.hideturtle()

def grav():
    my_pos = birdy.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    birdy.goto(x_pos, (y_pos - 10))
    turtle.ontimer(grav, 50)
    if birdy.pos()[1] > 410:
        draw.write("GAME OVER!", font=("Arial", 30, "normal"),align="center")
        time.sleep(2)
        quit()
    if birdy.pos()[1] < -410:
        draw.write("GAME OVER!", font=("Arial", 30, "normal"),align="center")
        time.sleep(2)
        quit()

grav()

def up():
    for i in range(7):
        my_pos = birdy.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        birdy.goto(x_pos, y_pos + 10)
    
turtle.onkeypress(up, UP_ARROW)
turtle.listen()


SIZE_X=1200
SIZE_Y=900
turtle.setup(SIZE_X,SIZE_Y)
turtle.bgcolor("light blue")

global food_stamp,food_pos
if birdy.pos() in food_pos:
    global score
    food_ind=food_pos.index(birdy.pos())
    food.clearstamp(food_stamp[food_ind])
    food_stamp.pop(food_ind)
    food_pos.pop(food_ind)
    score+=1
    scorePen = turtle.clone()
    scorePen.color("light blue")
    scorePen.shape("square")
    scorePen.hideturtle()
    scorePen.penup()
    scorePen.goto(230, 192)
    scorePen.stamp()
    scorePen.goto(230 + SQUARE_SIZE, 192)
    scorePen.stamp()
    scorePen.goto(125,175)
    scorePen.color("black")
    scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
    print("you have eaten the food and scored one point!!!")
    scorePen.color("white")
    scorePen.circle(30)
    make_food()

