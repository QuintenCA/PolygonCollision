import math
import line
import turtle
import time
import hitbox

# Returns a number rounded to 6 digits after the decimal
def round2(number):
	return round(number * 1000000) / 1000000

class Polygon:
	def __init__(self, sides, size):
		if sides < 1:
			return
		
		self.x = 0
		self.y = 0
		self.sides = sides
		self.size = size
		self.rotation = 0
		
	# Converts the rotation to radians
	def rads(self):
		return math.radians(self.rotation)
		
	# Returns the x coordinate of the hitbox's position
	def xcor(self):
		return round2(self.x)
	
	# Returns the y coordinate of the hitbox's position
	def ycor(self):
		return round2(self.y)
		
	# Sets the hitbox's coordinates to the given values.
	# If only one variable is given, it is assumed that it's value is actually a coordinate pair
	def goto(self, x, y=None):
		if y is None:
			self.x = x[0]
			self.y = x[1]
		else:
			self.x = x
			self.y = y
			
	def center(self):
		return (self.x, self.y)
	
	def hypo(self):
		return self.size
	
	def vertices(self):
		vertices = []
		angles = (2 * math.pi) / self.sides
		
		for i in range(self.sides):
			x = self.xcor() + (self.size * math.cos(angles * i + self.rads()))
			y = self.ycor() + (self.size * math.sin(angles * i + self.rads()))
			vertices.append((x, y))
		
		return vertices
	
	def edges(self):
		edges = []
		
		for i in range(self.sides):
			edge = line.Line(self.vertices()[i], self.vertices()[(i+1)%self.sides])
			edges.append(edge)
			
		return edges
		
		
	# Returns True if the given point is inside the hitbox
	def surrounds(self, point):
		total = 0
		for edge in self.edges():
			edge_angle = edge.angle()
			point_angle = line.Line(edge.p1, point).angle()
			new_angle = line.Line(edge.p1, point_angle - edge_angle, edge.length()).angle()
			if new_angle >= 0:
				total += 1
			else:
				total -= 1
		
		if abs(total) == len(self.edges()):
			return True
		return False
		
		
	# Returns the averaged coordinates of all points of both hitboxes that are inside the opposite hitbox
	# This is used to determine a single point of impact between the two hitboxes
	# Returns False if neither hitbox has a vertex inside the other
	def collision(self, other):
		distance = line.Line(self.center(), other.center()).length()
		if distance > self.hypo() + other.hypo():
			return False
		
		impacts = []
		
		for vertex in self.vertices():
			if other.surrounds(vertex):
				impacts.append(vertex)
		
		for vertex in other.vertices():
			if self.surrounds(vertex):
				impacts.append(vertex)
		
		if len(impacts) == 1:
			return impacts[0]
		
		if len(impacts) > 1:
			x = 0
			y = 0
			for i in impacts:
				x += i[0]
				y += i[1]
			
			x = round2(x / len(impacts))
			y = round2(y / len(impacts))
			
			return x, y
		
		return False