from OpenGL.GL import *
from OpenGL.GLU import *
from constants import colors
from utils import figures


def leg3D(size, kx=1, ky=1, kz=1):
    face = (
        (1,2,1),
        (-1,2,1),
        (-1,-2,1),
        (1,-2,1)
    )

    base = (
        (1,1,1),
        (-1,1,1),
        (-1,-1,1),
        (1,-1,1)
    )

    glScalef(size*kx, size*ky, size*kz)

    faces_r = [
        (0,0,0,0), # frente (no es necesario)
        (90,0,1,0), # derecha
        (-90,0,1,0), # izquierda
        (-180,0,1,0), # atras
    ]
    bases_r = [
        (0, -1, 0), # abajo
        (0, 3, 0) # arriba
    ]

    for face_r in faces_r:
        glPushMatrix()
        glRotatef(*face_r)
        figures.rectangle(colors.RGB_spanish_orange, face, colors.RGB_WHITE)
        glPopMatrix()

    for base_r in bases_r:
        glPushMatrix()
        glTranslatef(*base_r)
        glRotatef(90, 1, 0 ,0)
        figures.square(colors.RGB_spanish_orange, base, colors.RGB_WHITE)
        glPopMatrix()

def top3D(size, kx=1, ky=1, kz=1):
    vertices = (
        (1,2,1),
        (-1,2,1),
        (-1,-2,1),
        (1,-2,1)
    )

    face = (
        (1,1,1),
        (-1,1,1),
        (-1,-1,1),
        (1,-1,1)
    )

    glScalef(size*kx, size*ky, size*kz)

    # base abajo
    glPushMatrix()
    figures.rectangle(colors.RGB_ruby_red, vertices, colors.RGB_WHITE)
    glPopMatrix()

     # base arriba
    glPushMatrix()
    glRotatef(-180,0,1,0)
    figures.rectangle(colors.RGB_ruby_red, vertices, colors.RGB_WHITE)
    glPopMatrix()

    # cara derecha
    glPushMatrix()
    glRotatef(90,0,1,0)
    figures.rectangle(colors.RGB_ruby_red, vertices, colors.RGB_WHITE)
    glPopMatrix()
    
    # cara izq.
    glPushMatrix()
    glRotatef(-90,0,1,0)
    figures.rectangle(colors.RGB_ruby_red, vertices, colors.RGB_WHITE)
    glPopMatrix()
    
    # cara frente
    glPushMatrix()
    glTranslatef(0, 1, 0)
    glRotatef(180,0,1,1)
    figures.square(colors.RGB_ruby_red, face, colors.RGB_WHITE)
    glPopMatrix()

    # cara atras
    glPushMatrix()
    glTranslatef(0, -3, 0)
    glRotatef(180,0,1,1)
    figures.square(colors.RGB_ruby_red, face, colors.RGB_WHITE)
    glPopMatrix()


def table(size):
    glScalef(size, size, size)

    legs_t = [
        (0,0,0), # no es necesario
        (5,0,0),
        (0,0,5),
        (5,0,5)
    ]
    # render de las patas
    for leg in legs_t:
        glPushMatrix()
        glTranslatef(*leg)
        leg3D(1)
        glPopMatrix()

    # render del top
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glTranslatef(2.5, 2.5, -2.5)
    top3D(4.5, 0.8, 0.4, 0.1)
    glPopMatrix()


def chair(size):
    table(size)
    
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    glTranslatef(-2.5, 6.5, 1.5)
    top3D(4.5, 0.8, 0.4, 0.1)
    glPopMatrix()