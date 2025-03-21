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
	
	@staticmethod
	def bresenham_line(x0, y0, x1, y1):
	"""
	Generates the points on a line between (x0, y0) and (x1, y1) using Bresenham's algorithm.
	"""
	points = []
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	sx = 1 if x0 < x1 else -1
	sy = 1 if y0 < y1 else -1
	err = (dx > dy) - 0.5

	while True:
		points.append((x0, y0))
		if x0 == x1 and y0 == y1:
			break
		e2 = err
		if e2 > -dx:
			err -= dy
			x0 += sx
		if e2 < dy:
			err += dx
			y0 += sy
	return points

