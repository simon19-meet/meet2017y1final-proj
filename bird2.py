import turtle
import time

timing = 0

turtle.hideturtle()
turtle.register_shape("newnewnew_bird.gif")
turtle.register_shape("poof.gif")

writer = turtle.clone()
writer.hideturtle()
writer.penup()
writer.goto(200, 250)
writer.write("This way to Kenya -->", font=("Arial", 24, "normal"))
writer.goto(200, 210)
writer.write("get there to give the", font=("Arial", 24, "normal"))
writer.goto(200, 170)
writer.write("children food!", font=("Arial", 24, "normal"))


birdy = turtle.clone()
birdy.shape("newnewnew_bird.gif")
birdy.penup()
birdy.showturtle()

score = turtle.clone()
score.penup()
score.hideturtle()
score.goto(-500, 250)

UP_ARROW = "Up"
LEFT_ARROW = "Left"

draw = turtle.clone()
draw.hideturtle()
def times():
    global time
    timing += 1

def grav():
    global timing
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
    timing += 1
    score.clear()
    score.write("Time to reach Kenya: " + str(300 - timing), font=("Arial", 24, "normal"))
    if timing == 300:
        draw.write("You won!", font=("Ariel", 30, "normal"),align="center")
        time.sleep(3)
        quit()
def red():
    turtle.bgcolor("red")
turtle.onkeypress(red, LEFT_ARROW)

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

