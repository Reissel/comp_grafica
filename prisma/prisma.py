from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
quadro = 0
n = 50
a = 0


def desenhaBase():
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex2f(0,0)
    raio = 0.7
    for i in range(0,n+1):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex2f(x,y)
    glEnd()

def desenhaLados():
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex2f(0,0)
    raio = 0.7
    for i in range(0,n+1):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x,y,2)
    glEnd()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,1,1,1)
    desenhaBase()
    glTranslatef(0,0,-2)
    desenhaLados()
    glPopMatrix()
    glutSwapBuffers()
    a -= 1

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Prisma")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-8)
glutTimerFunc(50,timer,1)
glutMainLoop()