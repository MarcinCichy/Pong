from turtle import Turtle
import random


class Ball(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.setpos(position)
		self.right_move = random.randint(0, 180)
		self.left_move = random.randint(180, 360)
		self.setheading(self.right_move)
		self.ball_speed = 4

	def new_angle(self, side):
		right_list = [(0, 60), (300, 360)]
		right = random.choice(right_list)
		self.right_move = random.randint(right[0], right[1])
		self.left_move = random.randint(120, 240)
		self.setpos(0, 0)
		if side == "left":
			self.setheading(self.right_move)
		elif side == "right":
			self.setheading(self.left_move)

	def move(self):
		self.forward(self.ball_speed)

	def y_bounce(self):
		angle = self.heading()
		new_angle = 360 - angle
		self.setheading(new_angle)

	def x_bounce(self):
		angle = self.heading()
		new_angle = 180 - angle
		self.setheading(new_angle)
		self.ball_speed += 0.5

