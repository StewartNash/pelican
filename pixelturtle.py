import math

class PixelTurtle:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.angle = 0
		self.is_down = True

		self.x_maximum = 720
		self.y_maximum = 480
		self.x_minimum = 0
		self.y_minimum = 0

	def up(self):
		self.is_down = False

	def down(self):
		self.is_down = True

	def forward(self, distance):
		self.x = self.x + distance * math.cos(self.angle)
		self.y = self.y + distance * math.sin(self.angle)
	
