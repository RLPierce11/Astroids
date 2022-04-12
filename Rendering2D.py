from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def hex_to_rgb(hex):
	rgb = []
	for i in (0, 2, 4):
		decimal = int(hex[i:i+2], 16)
		rgb.append(decimal)

	return tuple(rgb)

def fill(color):
	#convert hexadecimal to rgb
	rgb = hex_to_rgb(color)
	glColor3f(rgb[0], rgb[1], rgb[2])


def pSize(numf):
	glPointSize(numf)

def point(x, y):
	glBegin(GL_POINTS)
	glVertex2f(x, y)
	glEnd()

def lWidth(numf):
	glLineWidth(numf)
	glPointSize(numf)

def line(x1, y1, x2, y2):
	glBegin(GL_LINES)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2)
	glEnd()


def arc(cx, cy, radius, stheta, etheta):
	x = cx + radius
	y = cy
	glBegin(GL_POINTS)
	while(stheta < etheta):
		rotx = cx + radius * math.cos(stheta * math.pi / 180)
		roty = cy + radius * math.sin(stheta * math.pi / 180)
		glVertex2f(rotx, roty)
		stheta += 1
	glEnd()

def ellipse_arc(cx, cy, width, height, stheta, etheta):
	x = cx + width
	y = cy
	glBegin(GL_POINTS)
	while(stheta < etheta):
		rotx = cx - (width * math.cos(stheta * math.pi / 180))
		roty = cy + (height * math.sin(stheta * math.pi / 180))
		glVertex2f(rotx, roty)
		stheta += 1
	glEnd()
	

def triangle(x1, y1, x2, y2, x3, y3):
	glBegin(GL_TRIANGLES)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2)
	glVertex2f(x3, y3)
	glEnd()

def rect(x1, y1, x2, y2, x3, y3, x4, y4):
	glBegin(GL_QUADS)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2)
	glVertex2f(x3, y3)
	glVertex2f(x4, y4)
	glEnd()

def circle(x1, y1, radius):
	theta = 0
	x = x1 + radius
	y = y1
	glBegin(GL_TRIANGLES)
	while(theta <= 360):
		rotx = x1 + radius * math.cos(theta * math.pi / 180)
		roty = y1 + radius * math.sin(theta * math.pi / 180)
		glVertex2f(rotx, roty)
		glVertex2f(x1, y1)
		glVertex2f(x, y)
		x = rotx
		y = roty
		theta += 1
	glEnd()


def ellipse(x1, y1, width, height):
	theta = 0
	x = x1 + width
	y = y1
	glBegin(GL_TRIANGLES)
	while(theta <= 360):
		rotx = x1 - (width * math.cos(theta * math.pi / 180))
		roty = y1 + (height * math.sin(theta * math.pi / 180))
		glVertex2f(rotx, roty)
		glVertex2f(x1, y1)
		glVertex2f(x, y)
		x = rotx
		y = roty
		theta += 1
	glEnd()





