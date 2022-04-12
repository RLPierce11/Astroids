#astroids game
from Rendering2D import *
from Vector3n import *
import math 
import random

class Ship:
	def __init__(self, x, y):
		self.pos = Vector3n(x, y, 0)
		self.top = Vector3n(x + 30, y, 0)
		self.left = Vector3n(math.cos(-120 * math.pi / 180) * (self.top.x - self.pos.x) - math.sin(-120 * math.pi / 180) * (self.top.y - self.pos.y) + self.pos.x, 
							 math.sin(-120 * math.pi / 180) * (self.top.x - self.pos.x) + math.cos(-120 * math.pi / 180) * (self.top.y - self.pos.y) + self.pos.y, 
							 0)
		self.right = Vector3n(math.cos(120 * math.pi / 180) * (self.top.x - self.pos.x) - math.sin(120 * math.pi / 180) * (self.top.y - self.pos.y) + self.pos.x, 
							  math.sin(120 * math.pi / 180) * (self.top.x - self.pos.x) + math.cos(120 * math.pi / 180) * (self.top.y - self.pos.y) + self.pos.y, 
							  0)

		self.vel = Vector3n(0, 0, 0)
		self.acc = Vector3n(0, 0, 0)

		self.heading = 0 

	def show(self):
		fill("FFFFFF")
		lWidth(2.0)
		line(self.top.x, self.top.y, self.right.x, self.right.y)
		line(self.top.x, self.top.y, self.left.x, self.left.y)
		line(self.right.x, self.right.y, self.pos.x, self.pos.y)
		line(self.left.x, self.left.y, self.pos.x, self.pos.y)

	def update(self):
		damping = 0.995

		self.vel = self.vel + self.acc
		self.vel.multS_S(damping)

		#limit topspeed of ship to 6
		if(self.vel.x > 7):
			self.vel.x = 7
		if(self.vel.y > 7):
			self.vel.y = 7

		self.pos = self.pos + self.vel
		#-----------------
		self.top = self.top + self.vel
		self.left = self.left + self.vel
		self.right = self.right + self.vel
		#---------------------
		self.acc.multS_S(0)

	def applyForce(self, force):
		self.acc = self.acc + force

	def turn(self, a):
		self.heading += a
		self.top = self.top.rotate(self.pos, a)
		self.left = self.left.rotate(self.pos, a)
		self.right = self.right.rotate(self.pos, a)

	def thrust(self):
		angle = self.heading #+ math.pi / 2
		force = Vector3n(round(math.cos(angle * math.pi / 180), 5), round(math.sin(angle * math.pi / 180), 5), 0)
		force.multS_S(0.1)
		self.applyForce(force)

	def wrapEdges(self):
		buffer = 30 * 2
		if(self.pos.x > 1000 + buffer):
			self.pos.x = self.pos.x - (1000 + buffer)
			self.top.x = self.top.x - (1000 + buffer)
			self.left.x = self.left.x - (1000 + buffer) 
			self.right.x = self.right.x - (1000 + buffer)
		elif(self.pos.x < -buffer):
			self.pos.x = self.pos.x + 1000 + buffer
			self.top.x = self.top.x + 1000 + buffer
			self.left.x = self.left.x + 1000 + buffer
			self.right.x = self.right.x + 1000 + buffer


		if(self.pos.y > 750 + buffer):
			self.pos.y = self.pos.y - (750 + buffer)
			self.top.y = self.top.y - (750 + buffer)
			self.left.y = self.left.y - (750 + buffer)
			self.right.y = self.right.y - (750 + buffer)
		elif(self.pos.y < buffer):
			self.pos.y = self.pos.y + 750 + buffer
			self.top.y = self.top.y + 750 + buffer
			self.left.y = self.left.y + 750 + buffer
			self.right.y = self.right.y + 750 + buffer
			


class Lastroid:
	def __init__(self, x, y):
		self.pos = Vector3n(x, y, 0)
		vx = round(random.uniform(-1.0, 1.0), 2)
		vy = round(random.uniform(-1.0, 1.0), 2)

		if(vx == 0 and vy == 0):
			vx = 0.5
			vy = -1.0

		self.vel = Vector3n(vx, vy, 0)
		self.hitpoints = 5

	def update(self):
		self.pos = self.pos + self.vel

	def collision(self, ship):
		if(ship.top.x > self.pos.x - 40 and ship.top.x < self.pos.x + 40 and ship.top.y > self.pos.y - 30 and ship.top.y < self.pos.y + 30):
			return True
		elif(ship.left.x > self.pos.x - 40 and ship.left.x < self.pos.x + 40 and ship.left.y > self.pos.y - 30 and ship.left.y < self.pos.y + 30):
			return True
		elif(ship.right.x > self.pos.x - 40 and ship.right.x < self.pos.x + 40 and ship.right.y > self.pos.y - 30 and ship.right.y < self.pos.y + 30):
			return True
		return False

	def hit(self, laser):
		if(laser.end.x > self.pos.x - 35 and laser.end.x < self.pos.x + 35 and laser.end.y > self.pos.y - 25 and laser.end.y < self.pos.y + 25):
			self.hitpoints = self.hitpoints - 1
			return True
		return False

	def get_hitpoints(self):
		return self.hitpoints


	def show(self):
		lWidth(2.0)
		x1 = self.pos.x - 40
		y1 = self.pos.y
		x2 = x1 + 20
		y2 = y1  + 30
		x3 = x2 + 30
		y3 = y2
		x4 = x3 + 30 
		y4 = y3 - 30
		x5 = x4
		y5 = y4 - 30
		x6 = x5 - 80
		y6 = y5
		x7 = x6 + 20
		y7 = y6 + 10

		line(x1, y1, x2, y2)
		line(x2, y2, x3, y3)
		line(x3, y3, x4, y4)
		line(x4, y4, x5, y5)
		line(x5, y5, x6, y6)
		line(x6, y6, x7, y7)
		line(x7, y7, x1, y1)

	def wrapEdges(self):
		buffer = 30 * 2
		if(self.pos.x > 1000 + buffer):
			self.pos.x = self.pos.x - (1000 + buffer)
		elif(self.pos.x < -buffer):
			self.pos.x = self.pos.x + 1000 + buffer

		if(self.pos.y > 750 + buffer):
			self.pos.y = self.pos.y - (750 + buffer)
		elif(self.pos.y < buffer):
			self.pos.y = self.pos.y + 750 + buffer

class Mastroid:
	def __init__(self, x, y):
		self.pos = Vector3n(x, y, 0)
		vx = round(random.uniform(-1.0, 1.0), 2)
		vy = round(random.uniform(-1.0, 1.0), 2)

		if(vx == 0 and vy == 0):
			vx = 0.5
			vy = -1.0

		self.vel = Vector3n(vx, vy, 0)
		self.hitpoints = 5

	def update(self):
		self.pos = self.pos + self.vel

	def show(self):
		lWidth(2.0)
		x1 = self.pos.x - 10
		y1 = self.pos.y
		x2 = x1 - 10
		y2 = y1 + 10
		x3 = x2 + 30
		y3 = y2 + 10
		x4 = x3 + 20
		y4 = y3 - 10
		x5 = x4 - 10
		y5 = y4 - 10
		x6 = x5 + 10
		y6 = y5 - 10
		x7 = x6 - 20
		y7 = y6 - 10
		x8 = x7 - 20
		y8 = y7 + 10
		x9 = x8 - 10
		y9 = y8

		line(x1, y1, x2, y2)
		line(x2, y2, x3, y3)
		line(x3, y3, x4, y4)
		line(x4, y4, x5, y5)
		line(x5, y5, x6, y6)
		line(x6, y6, x7, y7)
		line(x7, y7, x8, y8)
		line(x8, y8, x9, y9)
		line(x9, y9, x1, y1)

	def wrapEdges(self):
		buffer = 30 * 2
		if(self.pos.x > 1000 + buffer):
			self.pos.x = self.pos.x - (1000 + buffer)
		elif(self.pos.x < -buffer):
			self.pos.x = self.pos.x + 1000 + buffer

		if(self.pos.y > 750 + buffer):
			self.pos.y = self.pos.y - (750 + buffer)
		elif(self.pos.y < buffer):
			self.pos.y = self.pos.y + 750 + buffer

	def collision(self, ship):
		if(ship.top.x > self.pos.x - 25 and ship.top.x < self.pos.x + 25 and ship.top.y > self.pos.y - 20 and ship.top.y < self.pos.y + 20):
			return True
		elif(ship.left.x > self.pos.x - 25 and ship.left.x < self.pos.x + 25 and ship.left.y > self.pos.y - 20 and ship.left.y < self.pos.y + 20):
			return True
		elif(ship.right.x > self.pos.x - 25 and ship.right.x < self.pos.x + 25 and ship.right.y > self.pos.y - 20 and ship.right.y < self.pos.y + 20):
			return True
		return False

	def hit(self, laser):
		if(laser.end.x > self.pos.x - 25 and laser.end.x < self.pos.x + 25 and laser.end.y > self.pos.y - 15 and laser.end.y < self.pos.y + 15):
			self.hitpoints = self.hitpoints - 1
			return True
		return False

	def get_hitpoints(self):
		return self.hitpoints



class Sastroid:
	def __init__(self, x, y):
		self.pos = Vector3n(x, y, 0)
		vx = round(random.uniform(-1.0, 1.0), 2)
		vy = round(random.uniform(-1.0, 1.0), 2)

		if(vx == 0 and vy == 0):
			vx = 0.5
			vy = -1.0

		self.vel = Vector3n(vx, vy, 0)
		self.hitpoints = 5

	def update(self):
		self.pos = self.pos + self.vel

	def show(self):
		lWidth(2.0)
		x1 = self.pos.x - 15
		y1 = self.pos.y
		x2 = x1 + 10
		y2 = y1 + 10
		x3 = x2 + 10
		y3 = y2 
		x4 = x3 + 5
		y4 = y3 - 5
		x5 = x4 
		y5 = y4 - 10
		x6 = x5 - 20
		y6 = y5 

		line(x1, y1, x2, y2)
		line(x2, y2, x3, y3)
		line(x3, y3, x4, y4)
		line(x4, y4, x5, y5)
		line(x5, y5, x6, y6)
		line(x6, y6, x1, y1)

	def wrapEdges(self):
		buffer = 30 * 2
		if(self.pos.x > 1000 + buffer):
			self.pos.x = self.pos.x - (1000 + buffer)
		elif(self.pos.x < -buffer):
			self.pos.x = self.pos.x + 1000 + buffer

		if(self.pos.y > 750 + buffer):
			self.pos.y = self.pos.y - (750 + buffer)
		elif(self.pos.y < buffer):
			self.pos.y = self.pos.y + 750 + buffer

	def collision(self, ship):
		if(ship.top.x > self.pos.x - 7.5 and ship.top.x < self.pos.x + 7.5 and ship.top.y > self.pos.y - 12.5 and ship.top.y < self.pos.y + 12.5):
			return True
		elif(ship.left.x > self.pos.x - 7.5 and ship.left.x < self.pos.x + 7.5 and ship.left.y > self.pos.y - 12.5 and ship.left.y < self.pos.y + 12.5):
			return True
		elif(ship.right.x > self.pos.x - 7.5 and ship.right.x < self.pos.x + 7.5 and ship.right.y > self.pos.y - 12.5 and ship.right.y < self.pos.y + 12.5):
			return True
		return False

	def hit(self, laser):
		if(laser.end.x > self.pos.x - 20 and laser.end.x < self.pos.x + 20 and laser.end.y > self.pos.y - 10 and laser.end.y < self.pos.y + 10):
			self.hitpoints = self.hitpoints - 1
			return True
		return False

	def get_hitpoints(self):
		return self.hitpoints


class laser:
	def __init__(self, sx, sy, ex, ey, heading):
		self.start = Vector3n(sx, sy, 0)
		self.end = Vector3n(ex, ey, 0)

		self.vel = Vector3n(round(math.cos(heading * math.pi / 180), 5) * 3.5, round(math.sin(heading * math.pi / 180), 5) * 3.5, 0)

	def show(self):
		lWidth(3.0)
		line(self.start.x, self.start.y, self.end.x, self.end.y)

	def update(self):
		self.start = self.start + self.vel
		self.end = self.end + self.vel

	def edge(self):
		buffer = 30 * 2
		if(self.end.x > 1000 + buffer or self.end.x < 0 - buffer or self.end.y > 750 + buffer or self.end.y < 0 - buffer):
			return True
		return False




