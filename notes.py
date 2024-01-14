import turtle
from turtle import Turtle, Screen

# objects and their methods
screen = Screen()
paddle = Turtle()

# sets size and colour of screen attributes
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")

# sets paddle position and other attributes
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.speed("fastest")
paddle.setpos(350, 0)


# paddles controls
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

screen.exitonclick()
