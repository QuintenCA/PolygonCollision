import math
import line

class Hitbox:
	
	def __init__(self, width=20, height=20):
		self.xcor = 0
		self.ycor = 0
		self.width = width
		self.height = height
		self.border = 4
		self.rotation = 0
	
	def rads(self):
		return math.radians(self.rotation)
	
	def half_y(self):
		return round(self.height / 2)
	
	def half_x(self):
		return round(self.width / 2)
	
	def hypo(self):
		return math.sqrt(self.half_x() ** 2 + self.half_y() ** 2)
	
	def p1(self):
		angle = self.rads() + math.atan2(self.half_y(), self.half_x())
		point = (round(self.xcor + self.hypo() * math.cos(angle)),
		         round(self.ycor + self.hypo() * math.sin(angle)))
		return point
	
	def p2(self):
		angle = self.rads() + math.atan2(self.half_x(), self.half_y()) + (math.pi / 2)
		point = (round(self.xcor + self.hypo() * math.cos(angle)),
		         round(self.ycor + self.hypo() * math.sin(angle)))
		return point
	
	def p3(self):
		angle = self.rads() + math.atan2(self.half_y(), self.half_x()) + math.pi
		point = (round(self.xcor + self.hypo() * math.cos(angle)),
		         round(self.ycor + self.hypo() * math.sin(angle)))
		return point
	
	def p4(self):
		angle = self.rads() - math.atan2(self.half_y(), self.half_x())
		point = (round(self.xcor + self.hypo() * math.cos(angle)),
		         round(self.ycor + self.hypo() * math.sin(angle)))
		return point
	
	def goto(self, x, y):
		self.xcor = x
		self.ycor = y
	
	def ontop(self, hitbox):
		angle = math.radians(hitbox.rotation + 90)
		x = self.xcor + (math.cos(angle) * (self.half_x() + hitbox.half_x()))
		y = self.ycor + (math.sin(angle) * (self.half_y() + hitbox.half_y()))
		self.goto(x, y)

	def onbottom(self, hitbox):
		self.goto(self.xcor, hitbox.ycor - (self.half_y() + hitbox.half_y()))
	
	def onleft(self, hitbox):
		self.goto(hitbox.xcor - (self.half_x() + hitbox.half_x()), self.ycor)
	
	def onright(self, hitbox):
		self.goto(hitbox.xcor + (self.half_x() + hitbox.half_x()), self.ycor)
	
	def to(self, hitbox):
		self.goto(hitbox.xcor, hitbox.ycor)
	
	def center(self):
		point = (self.xcor, self.ycor)
		return point
	
	def top(self):
		box = Hitbox(self.width, self.border)
		box.goto(self.xcor, self.ycor + self.half_y())
		return box
	
	def bottom(self):
		box = Hitbox(self.width, self.border)
		box.goto(self.xcor, self.ycor - self.half_y())
		return box
	
	def left(self):
		box = Hitbox(self.border, self.height)
		box.goto(self.xcor - self.half_x(), self.ycor)
		return box
	
	def right(self):
		box = Hitbox(self.border, self.height)
		box.goto(self.xcor + self.half_x(), self.ycor)
		return box
	
	def edge1(self):
		return line.Line(self.p1(), self.p2())
	
	def edge2(self):
		return line.Line(self.p2(), self.p3())
	
	def edge3(self):
		return line.Line(self.p3(), self.p4())

	def edge4(self):
		return line.Line(self.p4(), self.p1())
	
	def vertices(self):
		return [self.p1(), self.p2(), self.p3(), self.p4()]
	
	def edges(self):
		return [self.edge1(), self.edge2(), self.edge3(), self.edge4()]
	
	def collide(self, other):
		for i in range(len(self.edges())):
			line1 = self.edges()[i]
			for j in range(len(self.edges())):
				line2 = other.edges()[j]
				
				if line1.intersect(line2):
					return True
		return False
		