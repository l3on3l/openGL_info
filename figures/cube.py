from OpenGL.GL import *
from OpenGL.GLU import *
from constants import colors
from utils import figures

def cube(size):
    vertices = (
        (-0.5, -0.5, 0.5),
        (0.5, -0.5, 0.5),
        (0.5, 0.5, 0.5),
        (-0.5, 0.5, 0.5)
    )
    # Vamos generando el cubo en base a transformaciones de cuadrados
    faces = [
        (colors.RGB_dark_orange ,(90,0,0,1)), # 1a cara = frente (por defecto)
        (colors.RGB_dark_orange ,(90,0,1,0)), # 2da cara = Derecha
        (colors.RGB_dark_orange ,(-90,0,1,0)), # 3a cara = Izquierda
        (colors.RGB_dark_orange ,(-180,0,1,0)), # 4a cara = Atras
        (colors.RGB_dark_orange ,(90,1,0,0)), # 5a cara = Arriba        
        (colors.RGB_dark_orange ,(-90,1,0,0)) # 6a cara = Abajo
    ]

    for (color, rotation) in faces:
        glPushMatrix()
        glScalef(size,size,size)
        glRotatef(rotation[0], rotation[1], rotation[2], rotation[3])
        figures.square(color, vertices, colors.RGB_WHITE)
        glPopMatrix()

