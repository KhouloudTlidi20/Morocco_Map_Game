import turtle
screen = turtle.Screen()
screen.title("Morocco Map Game")
image = "Map-of-Morocco.gif"
turtle.addshape(image)
turtle.shape(image)

# Get the coordinates  of a point


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

screen.mainloop() # Keep the screen active


screen.exitonclick()