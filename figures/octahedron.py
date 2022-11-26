from OpenGL.GL import *
from OpenGL.GLU import *
from constants import colors
from utils import figures

def octahedron(size):
    vertices = (
        (0.5, 0, 0),
        (0, 0.5, 0),
        (0, 0, 0.5),
    )
    figures.triangle3D(size, vertices, colors.RGB_ruby_red, colors.RGB_WHITE)
    glRotatef(-180, 0, 0, 1)
    figures.triangle3D(size, vertices, colors.RGB_ruby_red, colors.RGB_WHITE)


def octahedron2(size):
    # cara sentido horario x-y-z
    vertices = (
        (0.5, 0, 0),
        (0, 0.5, 0),
        (0, 0, 0.5),
    )

    faces = [
        (colors.RGB_dark_orange, (0, 0, 0, 0)), # 1ra cara = frente arriba (por defecto)
        (colors.RGB_dark_orange, (-90, 0, 1, 0)), # 2ra cara = izq. arriba
        (colors.RGB_dark_orange, (90, 0, 1, 0)), # 3ra cara = der. arriba
        (colors.RGB_dark_orange, (180, 0, 1, 0)), # 4ra cara = atras arriba
        (colors.RGB_ruby_red, (-90, 0, 0, 1)), # 5ta cara = frente abajo
        (colors.RGB_ruby_red, (180, 0, 0, 1)), # 6ta cara = izq. abajo
    ]

    for (color, rotation) in faces:
        glPushMatrix()
        glScalef(size,size,size)
        glRotatef(rotation[0], rotation[1], rotation[2], rotation[3])
        figures.triangle(color, vertices)
        glPopMatrix()
    
    # 7ma cara = der. abajo
    glPushMatrix()
    glScalef(size,size,size)
    glRotatef(90, 0, 1, 0)
    glRotatef(90, 1, 0, 0)
    figures.triangle(colors.RGB_ruby_red, vertices)
    glPopMatrix()

    # 8va cara = atras abajo
    glPushMatrix()
    glScalef(size,size,size)
    glRotatef(180, 0, 1, 0)
    glRotatef(90, 1, 0, 0)
    figures.triangle(colors.RGB_ruby_red, vertices)
    glPopMatrix()
