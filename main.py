import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
import numpy as np
from constants import colors

from utils import figures
from utils import primitives

from figures import cube
from figures import octahedron
from figures import star
from figures import table


def axis(sizeX, sizeY, sizeZ):
    #glPushMatrix()
    # Le decimos a OPENGL que interprete los vértices como líneas
    glBegin(GL_LINES)

    # Dibuja el eje x en rojo
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(sizeX, 0.0, 0.0)

    # Dibuja el eje y en verde
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, sizeY, 0.0)

    # Dibuja el eje z en azul
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, sizeZ)
    glEnd()
    #glPopMatrix()

def icosahedron2():
    PI = 3.141592
    GL_PI
    x, y, z, alpha, beta = 0 # Storage for coordinates and angles        
    radius = 60.0
    gradation = 20
    alpha = 0.0

    while(alpha < GL_PI):
        glBegin(GL_TRIANGLE_STRIP)
        beta = 0.0
        while( beta < 2.01*GL_PI):
            x = radius*cos(beta)*sin(alpha)
            y = radius*sin(beta)*sin(alpha)
            z = radius*cos(alpha)
            glVertex3f(x, y, z)
            x = radius*cos(beta)*sin(alpha + PI/gradation)
            y = radius*sin(beta)*sin(alpha + PI/gradation)
            z = radius*cos(alpha + PI/gradation)
            glVertex3f(x, y, z)
            beta += PI/gradation
        glEnd();
        alpha += PI/gradation

if __name__ == '__main__':
    pygame.init()
    screen = (700, 700)
    display = pygame.display.set_mode(screen, DOUBLEBUF|OPENGL)

    # Selecciona la matriz de proyeccion
    glMatrixMode(GL_PROJECTION)
    # Ángulo, ratio, near, far
    gluPerspective(45, (screen[0] / screen[1]), 0.1, 50)
    gluLookAt(0,0,5,0,0,0,0,1,0)
    button_down = False

    # Selecciona la matriz de MODELVIEW
    glMatrixMode(GL_MODELVIEW)  
    modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

    while True:
        glPushMatrix()
        glLoadIdentity()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # movemos los ejes para mover la figura
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
                # if event.key == pygame.K_r:
                #     glLoadIdentity()
                #     glTranslatef(0.0, 0.0, -5)

            # rotamos con el moviemiento del mouse los ejes x e y si hacemos click (manteniendo).
            if event.type == pygame.MOUSEMOTION:
                if button_down == True:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)
                # print(event.rel)

        # verificamos si hacemos click con el mouse
        for event in pygame.mouse.get_pressed():
            # print(pygame.mouse.get_pressed())
            if pygame.mouse.get_pressed()[0] == 1:
                button_down = True
            elif pygame.mouse.get_pressed()[0] == 0:
                button_down = False

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glMultMatrixf(modelMatrix)
        modelMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glLoadIdentity()
        glTranslatef(0, 0, -5)
        glMultMatrixf(modelMatrix)

        axis(3, 3, 3)
        cube.cube(1)
        # table.table(0.2)
        # table.chair(0.2)
        # octahedron.octahedron(3)
        # star.star4Pointer(1)
        # star.star5Pointer(1)
        # primitives.draw_cylinder(0.1, 1, colors.RGB_dark_orange)
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)
        

    
