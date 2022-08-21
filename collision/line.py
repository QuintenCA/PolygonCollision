import math
import turtle

class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
	def intersect(self, other):
		denominator = self.A() * other.B() - other.A() * self.B()
		if denominator == 0:
			return None
		
		x = (other.B() * self.C() - self.B() * other.C()) / denominator
		y = (self.A() * other.C() - other.A() * self.C()) / denominator
		
		point = (x, y)
		
		if not ((self.p1[0] <= x <= self.p2[0] or self.p2[0] <= x <= self.p1[0]) and
		        (self.p1[1] <= y <= self.p2[1] or self.p2[1] <= y <= self.p1[1])):
			return None
		
		if not ((other.p1[0] <= x <= other.p2[0] or other.p2[0] <= x <= other.p1[0]) and
		        (other.p1[1] <= y <= other.p2[1] or other.p2[1] <= y <= other.p1[1])):
			return None
		
		return point
	
	def length(self):
		dist = math.sqrt((self.xdist() ** 2) + self.ydist() ** 2)
		return dist
	
	def xdist(self):
		return self.p2[0] - self.p1[0]

	def ydist(self):
		return self.p2[1] - self.p1[1]
	
	def A(self):
		return self.p2[1] - self.p1[1]
	
	def B(self):
		return self.p1[0] - self.p2[0]
	
	def C(self):
		return self.A() * self.p1[0] + self.B() * self.p1[1]
	
	def center(self):
		point = (self.xdist() / 2, self.ydist() / 2)
		return point
	
	def angle(self):
		return math.atan2(self.ydist(), self.xdist())
		
		