import turtle

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
