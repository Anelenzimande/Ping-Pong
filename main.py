import time
from paddles import Paddles
from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard

# Objects and their methods
screen = Screen()
paddle = Turtle()
scoreboard = Scoreboard()
ball = Ball()

# Set size and color of screen attributes
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))

# Paddles controls
screen.tracer(0)  # Set up tracer

screen.listen()

# Right paddle controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# Left paddle controls
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Pong ball movement
def game_loop():
    screen.update()
    ball.move()

    # Detect collisions with boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collisions with paddles
    if (
        ball.distance(r_paddle) < 50 and ball.xcor() > 320
    ) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    screen.ontimer(game_loop, 20)  # Call the function again after 20 milliseconds

game_loop()  # Start the game loop

screen.exitonclick()
