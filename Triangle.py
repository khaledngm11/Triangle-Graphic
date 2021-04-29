import glfw
from OpenGL.GL import *
import numpy as np
import random
from math import sin,cos
if not glfw.init():
    raise Exception('Glfw not initialized !')

window=glfw.create_window(512, 512, 'Triangle', None, None)
glfw.set_window_pos(window, 200, 400)
if not window:
    glfw.terminate()
    raise Exception('window not created !')
glfw.make_context_current(window)
glClearColor(0.5,0.8,0.9,1)
ver=[-0.5,-0.5,0,
     0.5,-0.5,0,
     0.0,0.5,0.0 ]
col=[0.8,0.0,0.0,0.6,1.0,1.0,0.0,0.0,0.3]
     
ver=np.array(ver,dtype=np.float32)
col=np.array(col,dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3,GL_FLOAT,0,ver)   
glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3,GL_FLOAT,0,col)

while not glfw.window_should_close(window):
    ct=glfw.get_time()
    glfw.poll_events()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES,0,3)
    glLoadIdentity()
    glRotate(abs(sin(ct))*180,0,0,1)
    glScale(abs(sin(ct)),abs(sin(ct)),1)
    glTranslatef(sin(ct),cos(ct),0)
    glfw.swap_buffers(window)
glfw.terminate()