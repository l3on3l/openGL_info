from OpenGL.GL import *
from OpenGL.GLU import *

def square(rgb, vertices, lineRGB=None):
    r,g,b = rgb
    glColor3f(r,g,b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glEnd()
    if (lineRGB is not None):
        glColor3f(lineRGB[0], lineRGB[1], lineRGB[2])
        glBegin(GL_LINES)
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[0])
        glEnd()


def triangle(rgb, vertices, lineRGB=None):
    r,g,b = rgb
    glColor3f(r,g,b)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glEnd()
    if (lineRGB is not None):
        glColor3f(lineRGB[0], lineRGB[1], lineRGB[2])
        glBegin(GL_LINES)
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[1])
        glEnd()

def triangle3D(size, vertices, colorRGB, lineRGB=None):
    """dibuja un triangulo en 3D en el cuadrante xyz.
       Parametros:
        @size: tamanho escalado
        @vertices: puntos del triangulo que debe ser en sentido x-y-z
        @colorRGB: color del triangulo en RGB
        @lineRGB: color de las lineas (opcional)
    """

    faces = [
        (colorRGB, (0, 0, 0, 0)), # 1ra cara = frente arriba (por defecto)
        (colorRGB, (-90, 0, 1, 0)), # 2ra cara = izq. arriba
        (colorRGB, (90, 0, 1, 0)), # 3ra cara = der. arriba
        (colorRGB, (180, 0, 1, 0)), # 4ra cara = atras arriba
    ]

    for (color, rotation) in faces:
        glPushMatrix()
        glScalef(size,size,size)        
        glRotatef(rotation[0], rotation[1], rotation[2], rotation[3])
        triangle(color, vertices, lineRGB)
        glPopMatrix()

def rectangle(colorRGB, vertices, lineRGB):
    glColor3fv(colorRGB)
    glBegin(GL_QUADS)
    glVertex3fv(vertices[0])
    glVertex3fv(vertices[1])
    glVertex3fv(vertices[2])
    glVertex3fv(vertices[3])
    glEnd()
    if (lineRGB is not None):
        glColor3fv(lineRGB)
        glBegin(GL_LINES)
        glVertex3fv(vertices[0])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[1])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[2])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[3])
        glVertex3fv(vertices[0])
        glEnd()