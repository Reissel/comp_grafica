from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = yrot_terra = ytrans_terra = yrot_lua = ytrans_lua = 0.0
dx = 0.1
dy = 0
dz = 0

r = 1
n = 50
halfpi = math.pi/2

# texture = []

def LoadTextures():
    global texture
    texture = [ glGenTextures(1), glGenTextures(1), glGenTextures(1) ]

    ################################################################################
    ###### SOL ######
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='C:/Users/Reissel/Desktop/Computação Gráfica/comp_grafica/textura/8k_sun.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
    
    
    ###### TERRA ######
    glBindTexture(GL_TEXTURE_2D, texture[1])
    reader = png.Reader(filename='C:/Users/Reissel/Desktop/Computação Gráfica/comp_grafica/textura/mapa2.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

    ###### LUA ######
    glBindTexture(GL_TEXTURE_2D, texture[2])
    reader = png.Reader(filename='C:/Users/Reissel/Desktop/Computação Gráfica/comp_grafica/textura/2k_moon2.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def f_sun(u,v):
    theta =  (u*math.pi/(n-1)) - halfpi
    phi = (v*2*math.pi)/(n-1)
    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z

def f_terra(u,v):
    theta =  (u*math.pi/(n-1)) - halfpi
    phi = (v*2*math.pi)/(n-1)
    x = (r-0.75)*math.cos(theta)*math.cos(phi)
    y = (r-0.75)*math.sin(theta)
    z = (r-0.75)*math.cos(theta)*math.sin(phi)
    return x, y, z

def f_lua(u,v):
    theta =  (u*math.pi/(n-1)) - halfpi
    phi = (v*2*math.pi)/(n-1)
    x = (r-0.90)*math.cos(theta)*math.cos(phi)
    y = (r-0.90)*math.sin(theta)
    z = (r-0.90)*math.cos(theta)*math.sin(phi)
    return x, y, z

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture, yrot_terra, ytrans_terra, yrot_lua, ytrans_lua

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.0,0.0,0.0,1.0)

    ## SOL ##
    glTranslatef(0.0,0.0,-7.5)
    glRotatef(xrot,1.0,0.0,0.0)
    glRotatef(yrot,0.0,1.0,0.0)
    glRotatef(zrot,0.0,0.0,1.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[0])

    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            glTexCoord2f(i/n,j/n)
            glVertex3fv(f_sun(i,j))
            glTexCoord2f((i+1)/n,(j+1)/n)
            glVertex3fv(f_sun(i+1,j+1))
        glEnd()


    ## TERRA ##
    glRotatef(ytrans_terra,0.0,1.0,0.0)
    glTranslatef(0.0, 0.0, 2.0)
    glRotatef(yrot_terra,0.0,1.0,0.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[1])

    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            glTexCoord2f(i/n,j/n)
            glVertex3fv(f_terra(i,j))
            glTexCoord2f((i+1)/n,(j+1)/n)
            glVertex3fv(f_terra(i+1,j+1))
        glEnd()
    

    ## LUA ##
    glRotatef(ytrans_lua,0.0,1.0,0.0)
    glTranslatef(0.0, 0.0, 0.5)
    glRotatef(yrot_lua,0.0,1.0,0.0)
    
    glBindTexture(GL_TEXTURE_2D, texture[2])
    
    for i in range(n):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(n):
            glTexCoord2f(i/n,j/n)
            glVertex3fv(f_lua(i,j))
            glTexCoord2f((i+1)/n,(j+1)/n)
            glVertex3fv(f_lua(i+1,j+1))
        glEnd()
    
    
    #xrot = xrot + 0.01                # X rotation
    yrot = yrot + 1                # Y rotation
    #zrot = zrot + 0.01                 # Z rotation
    yrot_terra = yrot_terra + 10
    ytrans_terra = ytrans_terra + 4
    yrot_lua = yrot_lua + 2
    ytrans_lua = ytrans_lua + 2

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        dx = 1.0
        dy = 0
        dz = 0   
    elif tecla == b'y' or tecla == b'Y':
        dx = 0
        dy = 1.0
        dz = 0   
    elif tecla == b'z' or tecla == b'Z':
        dx = 0
        dy = 0
        dz = 1.0

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Sistema Solar")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(teclaEspecialPressionada)
    InitGL(640, 480)
    glutMainLoop()


main()
