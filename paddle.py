from turtle import Turtle




class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.shape("square")
		self.color("white")
		self.penup()
		self.setpos(position)
		self.shapesize(stretch_wid=1, stretch_len=5)
		self.setheading(90)

	def go_up(self):
		self.forward(20)

	def go_down(self):
		self.back(20)

