import turtle
turtle.hideturtle()
turtle.register_shape("newnew_bird.gif")

birdy = turtle.clone()
birdy.shape("newnew_bird.gif")
birdy.penup()
birdy.showturtle()

UP_ARROW = "Up"

def grav():
    my_pos = birdy.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    birdy.goto(x_pos, (y_pos - 5))
    turtle.ontimer(grav, 30)
    
grav()

def up():
    for i in range(10):
        my_pos = birdy.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        birdy.goto(x_pos, y_pos + 5)
    
turtle.onkeypress(up, UP_ARROW)
turtle.listen()


