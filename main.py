from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Vector3n import *
from astroids_and_ship import *

ship = Ship(500, 375)

largeA = [Lastroid(700, 500), Lastroid(700, 200), Lastroid(300, 600)]
mediumA = [Mastroid(375, 100), Mastroid(650, 375), Mastroid(200, 375)]
smallA = [Sastroid(100, 100), Sastroid(700, 800), Sastroid(900, 100), Sastroid(100, 375)]

lasers = []

width = 1000
height = 750

FPS = 60.0


def buttons(key, x, y):
	if(key == GLUT_KEY_UP):
		ship.thrust()
	elif(key == GLUT_KEY_LEFT):
		ship.turn(5.0)
	elif(key == GLUT_KEY_RIGHT):
		ship.turn(-5.0)
	elif(key == b' '):
		lasers.append(laser(ship.pos.x, ship.pos.y, ship.top.x, ship.top.y, ship.heading))

#ship collision
def ship_col(astroid, ship):
	if(astroid.collision(ship) == True):
		largeA.clear()
		mediumA.clear()
		smallA.clear()


def update(value):
	global FPS
	glutPostRedisplay()
	glutTimerFunc(int(1000/FPS), update, int(0))

def showScreen():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	iterate()


	ship.update()
	ship.wrapEdges()
	ship.show()

	for a in largeA:
		a.update()
		ship_col(a, ship)
		for l in lasers:
			if(a.hit(l) == True) :
				if(a.get_hitpoints() == 0):
					mediumA.append(Mastroid(a.pos.x, a.pos.y))
					mediumA.append(Mastroid(a.pos.x, a.pos.y))
					smallA.append(Sastroid(a.pos.x, a.pos.y))
					largeA.remove(a)
				lasers.remove(l)
		a.wrapEdges()
		a.show()
	for b in mediumA:
		b.update()
		ship_col(b, ship)
		for l in lasers:
			if(b.hit(l) == True): 
				if(b.get_hitpoints() == 0):
					smallA.append(Sastroid(b.pos.x, b.pos.y))
					smallA.append(Sastroid(b.pos.x, b.pos.y))
					smallA.append(Sastroid(b.pos.x, b.pos.y))
					mediumA.remove(b)
				lasers.remove(l)
		b.wrapEdges()
		b.show()
	for c in smallA:
		c.update()
		ship_col(c, ship)
		for l in lasers:
			if(c.hit(l) == True): 
				if(c.get_hitpoints() == 0):
					smallA.remove(c)
				lasers.remove(l)
		c.wrapEdges()
		c.show()
	for l in lasers:
		l.update()
		if(l.edge() == True):
			lasers.remove(l)
		l.show()





	glutSwapBuffers()

def iterate():
	glViewport(0, 0, width, height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0, 0)
	wind = glutCreateWindow("Astroids | Ryan's OpenGL Practice")
	glutDisplayFunc(showScreen)
	glutSpecialFunc(buttons)
	glutKeyboardFunc(buttons)
	#glutIdleFunc(showScreen)
	glutTimerFunc(int(0), update, int(0))
	glutMainLoop()


main()


