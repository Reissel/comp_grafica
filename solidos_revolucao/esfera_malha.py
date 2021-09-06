from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import numpy as np

r = 1
r1 = 0.5
R = 2
n = 50
halfpi = math.pi/2

def cor(t, c1 = np.array([1,0.5,0.5]), c2 = np.array([0,0.5,1])):
    return c1 + t*(c2 - c1)

def desenhaEsfera():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(n):
        theta =  (i*math.pi/(n-1)) - halfpi
        for j in range(n):
            phi = (j*2*math.pi)/(n-1)
            x = r*math.cos(theta)*math.cos(phi)
            y = r*math.sin(theta)
            z = r*math.cos(theta)*math.sin(phi)

            dtheta =  ((i+1)*math.pi/(n-1)) - halfpi
            dphi = ((j+1)*2*math.pi)/(n-1)
            dx = r*math.cos(dtheta)*math.cos(dphi)
            dy = r*math.sin(dtheta)
            dz = r*math.cos(dtheta)*math.sin(dphi)

            glVertex3f(x,y,z)
            glColor3fv(cor(i/(n-1)))
            glVertex3f(dx,dy,dz)
    glEnd()

a = 0

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glTranslate(0, 0, 0)
    glRotatef(-a,0.25,0.5,1)
    desenhaEsfera()
    glPopMatrix()
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    a += 5
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-15)
glutTimerFunc(50,timer,1)
glutMainLoop()


