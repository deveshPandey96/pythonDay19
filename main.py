from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.bk(10)

def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_anticlockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def reset():
    tim.reset()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_anticlockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(reset, "c")
screen.exitonclick()