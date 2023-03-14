import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
vertices=(
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1),
    )
edges=(
       (0,1),
       (0,3),
       (0,4),
       (2,1),
       (2,3),
       (2,7),
       (6,3),
       (6,4),
       (6,7),
       (5,1),
       (5,4),
       (5,7),
       )
surfaces=(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    )
colors=(
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,1,0),
        (1,0,1),
        (0,1,1),
        )
def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x=-1
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def draw():
    glutWireTeapot(0.5)
    glFlush()
def main():
    pygame.init()
    scrn=(800,600)
    pygame.display.set_mode(scrn,DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    sphere=gluNewQuadric()
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,(scrn[0]/scrn[1]),0.1,50.0)
    glTranslate(0.0,0.0,-5)
    glRotatef(0,0,0,0)
    stop=False
    while not stop:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #gluCylinder(sphere,1,1,10,100,10)
        #gluQuadricTexture(sphere,GLU_TRUE)
        glRotatef(100,200,300,10)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                stop=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslate(0.1,0,0)
                if event.key == pygame.K_d:
                    glTranslate(-0.1,0,0)
                if event.key == pygame.K_w:
                    glTranslate(0,0.1,0)
                if event.key == pygame.K_s:
                    glTranslate(0,-0.1,0)
                if event.key == pygame.K_LEFT:
                    glRotatef(2,0,-1,0)
                    glTranslate(0.1,0,0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(2,0,1,0)
                    glTranslate(-0.1,0,0)
                if event.key == pygame.K_UP:
                    glTranslate(0,-0.1,0)
                    glRotatef(2,-1,0,0)
                if event.key == pygame.K_DOWN:
                    glTranslate(0,0.1,0)
                    glRotatef(2,1,0,0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslate(0,0,1)
                if event.button == 5:
                    glTranslate(0,0,-1)
main()