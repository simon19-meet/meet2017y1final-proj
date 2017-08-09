import turtle

UP_ARROW = "Up"
bird = turtle.clone()
bird.shape("turtle")
bird.color("green")
bird.goto (0, 0)

def moveup():
    print("Hey")
    
turtle.onkeypress(moveup, UP_ARROW)
turtle.listen()
turtle.mainloop()
