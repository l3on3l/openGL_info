from OpenGL.GL import *
from OpenGL.GLU import *
from constants import colors
from utils import figures
import math
import numpy

def starPointer(colorRGB, lineRGB=None):
    vertices1 = [
        (0.5, 0, 0),
        (0, 1.5, 0),
        (0, -0.5, 0.5)
    ]
    vertices2 = [
        (-0.5, 0, 0),
        (0, 1.5, 0),
        (0, -0.5, 0.5)
    ]
    
    figures.triangle(colorRGB, vertices1, lineRGB)
    figures.triangle(colorRGB, vertices2, lineRGB)

def starPointer3D(size, colorRGB, lineRGB=None):
    faces = [
        (colorRGB, (-180, 0, 1, 0)), # 1ra cara = frente arriba (por defecto)
        (colorRGB, (0, 0, 0, 0))
    ]

    for (color, rotation) in faces:
        glPushMatrix()
        glScalef(size,size,size)        
        glRotatef(rotation[0], rotation[1], rotation[2], rotation[3])
        starPointer(colorRGB, lineRGB)
        glPopMatrix()

def star4Pointer(size):
    starPointer3D(size, colors.RGB_dark_orange, colors.RGB_WHITE)

    # abajo
    glRotatef(180, 1, 0, 0)
    glTranslatef(0, 1, 0)
    starPointer3D(size, colors.RGB_dark_orange, colors.RGB_WHITE)
    glTranslatef(0, -1, 0)

    # izq
    glRotatef(90, 0, 0, 1)
    glTranslatef(0.5, 0.5, 0)
    starPointer3D(size, colors.RGB_dark_orange, colors.RGB_WHITE)

    # der
    glRotatef(-180, 0, 0, 1)
    glTranslatef(0, 1, 0)
    starPointer3D(size, colors.RGB_dark_orange, colors.RGB_WHITE)

# @todo
def star5Pointer(size):
    vertices = [
        (0.5, 0, 0),
        (0, 1.5, 0),
        (0, -0.5, 0.5)
    ]
    figures.triangle3D(size, vertices, colors.RGB_electric_blue)
