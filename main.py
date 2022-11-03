import time
from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball



screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:

	screen.update()
	ball.move()
	time.sleep(0.01)

	#Detect wall collision
	if ball.ycor() > 290 or ball.ycor() < -290:
		ball.y_bounce()

	#Detect r_paddle collision
	if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
		ball.x_bounce()

	#Detect l_paddle collision
	if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
		ball.x_bounce()

	#Detect right miss
	if ball.xcor() > 390:
		time.sleep(0.5)
		ball.new_angle("right")
		ball.ball_speed = 4
		scoreboard.l_point()

	if ball.xcor() < -390:
		time.sleep(0.5)
		ball.new_angle("left")
		ball.ball_speed = 4
		scoreboard.r_point()






screen.exitonclick()