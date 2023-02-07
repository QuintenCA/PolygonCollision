import math
import line
import turtle
import time


# Returns a number rounded to 6 digits after the decimal
def round2(number):
	return round(number * 1000000) / 1000000

# A representation of a rectangle using four points. Can be rotated and used to check collision against other hitboxes.
class Hitbox:
	def __init__(self, width=20, height=20):
		self.x = 0
		self.y = 0
		self.width = width
		self.height = height
		self.border = 4
		self.rotation = 0
	
	# Converts the rotation to radians
	def rads(self):
		return math.radians(self.rotation)
	
	# Returns half of the height of the hitbox
	def half_y(self):
		return self.height / 2
	
	# Returns half of the width of the hitbox
	def half_x(self):
		return self.width / 2
	
	# Returns the x coordinate of the hitbox's position
	def xcor(self):
		return round2(self.x)
	
	# Returns the y coordinate of the hitbox's position
	def ycor(self):
		return round2(self.y)
	
	# Returns the hypotenuse of the half width and half height.
	# Used to determine the maximum distance a point can be from the center while still being in the shape.
	def hypo(self):
		return math.sqrt(self.half_x() ** 2 + self.half_y() ** 2)
	
	# Returns the coordinate pair of the upper right vertex of the rectangle.
	def p1(self):
		angle = self.rads() + math.atan2(self.half_y(), self.half_x())
		point = (round2(self.xcor() + self.hypo() * math.cos(angle)),
		         round2(self.ycor() + self.hypo() * math.sin(angle)))
		return point
	
	# Returns the coordinate pair of the upper left vertex of the rectangle.
	def p2(self):
		angle = self.rads() + math.atan2(self.half_x(), self.half_y()) + (math.pi / 2)
		point = (round2(self.xcor() + self.hypo() * math.cos(angle)),
		         round2(self.ycor() + self.hypo() * math.sin(angle)))
		return point
	
	# Returns the coordinate pair of the lower left vertex of the rectangle.
	def p3(self):
		angle = self.rads() + math.atan2(self.half_y(), self.half_x()) + math.pi
		point = (round2(self.xcor() + self.hypo() * math.cos(angle)),
		         round2(self.ycor() + self.hypo() * math.sin(angle)))
		return point
	
	# Returns the coordinate pair of the lower right vertex of the rectangle.
	def p4(self):
		angle = self.rads() - math.atan2(self.half_y(), self.half_x())
		point = (round(self.xcor() + self.hypo() * math.cos(angle)),
		         round(self.ycor() + self.hypo() * math.sin(angle)))
		return point
	
	# Sets the hitbox's coordinates to the given values.
	# If only one variable is given, it is assumed that it's value is actually a coordinate pair
	def goto(self, x, y=None):
		if y is None:
			self.x = x[0]
			self.y = x[1]
		else:
			self.x = x
			self.y = y
	
	# Returns the coordinate pair of the hitbox's center position
	def center(self):
		point = (self.xcor(), self.ycor())
		return point
	
	# Returns the top edge of the hitbox as a line object
	def edge1(self):
		return line.Line(self.p1(), self.p2())
	
	# Returns the left edge of the hitbox as a line object
	def edge2(self):
		return line.Line(self.p2(), self.p3())
	
	# Returns the bottom edge of the hitbox as a line object
	def edge3(self):
		return line.Line(self.p3(), self.p4())
	
	# Returns the right edge of the hitbox as a line object
	def edge4(self):
		return line.Line(self.p4(), self.p1())
	
	# Returns all the hitbox's vertices as a list
	def vertices(self):
		return [self.p1(), self.p2(), self.p3(), self.p4()]
	
	# Returns all the hitbox's vertices as a list
	def edges(self):
		return [self.edge1(), self.edge2(), self.edge3(), self.edge4()]

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
	
	def closest_edge(self, point):
		min_dist = math.inf
		close_edge = None
		for edge in self.edges():
			angle = line.Line(edge.center(), self.center()).angle()
			l = line.Line(point, angle + math.pi, self.hypo())
			edgepoint = l.intersect(edge)
			
			if edgepoint is None:
				distance = math.inf
			else:
				distance = line.Line(point, edgepoint).length()
			
			if distance < min_dist:
				min_dist = distance
				close_edge = edgepoint
		return close_edge
		
		
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
	
	
	def edgecollision(self, other):
		distance = line.Line(self.center(), other.center()).length()
		if distance > self.hypo() + other.hypo():
			return False
		
		impacts = []
		
		for edge1 in self.edges():
			for edge2 in other.edges():
				intersection = edge1.intersect(edge2)
				if intersection is not None:
					impacts.append(intersection)
		
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
