from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

def draw_cylinder(radius, height, colorRGB):
    x              = 0.0
    y              = 0.0
    angle          = 0.0
    angle_stepsize = 0.1
    # Draw the tube 
    glColor3fv(colorRGB)
    glBegin(GL_QUAD_STRIP)
    angle = 0.0
    while( angle < 2*pi ):
        x = radius * cos(angle)
        y = radius * sin(angle)
        glVertex3f(x, y , height)
        glVertex3f(x, y , 0.0)
        angle = angle + angle_stepsize
    
    glVertex3f(radius, 0.0, height)
    glVertex3f(radius, 0.0, 0.0)
    glEnd()

    # Draw the circle on top of cylinder
    glColor3fv(colorRGB)
    glBegin(GL_POLYGON)
    angle = 0.0
    while( angle < 2*pi ):
        x = radius * cos(angle)
        y = radius * sin(angle)
        glVertex3f(x, y , height)
        angle = angle + angle_stepsize
    glVertex3f(radius, 0.0, height)
    glEnd()

def sphere_triangle():
    radius = 1.0
    gradation = 20
    
    glColor3fv((1,0,0))
    alpha = 0.0
    while(alpha < pi):
        beta = 0.0
        glBegin(GL_TRIANGLE_STRIP)
        while(beta < 2.01*pi):
            x = radius*cos(beta)*sin(alpha)
            y = radius*sin(beta)*sin(alpha)
            z = radius*cos(alpha)
            glVertex3f(x, y, z)
            x = radius*cos(beta)*sin(alpha + pi/gradation)
            y = radius*sin(beta)*sin(alpha + pi/gradation)
            z = radius*cos(alpha + pi/gradation)        
            glVertex3f(x, y, z)
            beta += pi/gradation
        glEnd()
        alpha += pi/gradation