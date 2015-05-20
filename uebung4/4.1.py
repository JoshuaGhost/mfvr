import pygame
from time import clock
from math import sin, pi

poolwidth = 100
bar_width = 6
level = 50
waveheight = 50
wavelen = 20

offset_x = 100
offset_y = 300

delta_t = 0.01
wavespeed = 4.0
delta_x = 1.0

daempfung = 0.999 

waveseq = []
for i in range(wavelen+1):
    waveseq.append(waveheight*sin(i*pi/wavelen))

class Game(object):
    
    def __init__(self):
        pass    

    def __intgrt__(self, h, v):
        h[0] = h[1]
        h[-1] = h[-2]
        assert 1<=poolwidth-2
        for i in range(1, poolwidth+1):
            v[i] = v[i]+\
                   (delta_t*wavespeed**2/delta_x**2)*\
                   (h[i-1]-2*h[i]+h[i+1])
        
        for i in range(1, poolwidth+1):
            h[i] = level+(h[i]+delta_t*v[i]-level)*(daempfung)
        return h, v
        
    def setwave(self, h, center):
        for i in range(center-wavelen/2, center+wavelen/2+1):
            h[i+1] = level+waveseq[i-wavelen/2-center]
        return h

    def main(self, screen):

        x_scale, y_scals = screen.get_size()
        h = [level] * (poolwidth+2)
        v = [0]*(poolwidth+2)
        wavecenter = wavelen/2
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and\
                    event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.MOUSEMOTION:
                    (mousex, mousey) = pygame.mouse.get_pos()
                    wavecenter = (mousex-offset_x)/bar_width
                    wavecenter = wavecenter if wavecenter-(wavelen/2)>0 else wavelen/2
                    wavecenter = wavecenter if wavecenter+(wavelen/2)<poolwidth+1 else poolwidth-(wavelen/2)+1
                if event.type == pygame.MOUSEBUTTONDOWN and\
                    wavecenter <> wavelen/2 and\
                    wavecenter <> poolwidth-(wavelen/2)+1 and\
                    pygame.mouse.get_pressed()[0]:
                    h = self.setwave(h, wavecenter)
                
            screen.fill((200, 200, 200))
        
            for i in range(1, len(h)-1):
                try:
                    pygame.draw.rect(screen, (0,0,255),\
                                     (offset_x+i*bar_width,\
                                      offset_y-int(h[i] if h[i]>0 else 0),\
                                      bar_width,\
                                      int(h[i] if h[i]>0 else 0)),\
                                     0)
                except Exception, e:
                    print i, ' ', h[i]
                    print e
                    return 1
            if wavecenter <> wavelen/2 and\
                wavecenter <> poolwidth-(wavelen/2)+1:
                    for i in range(wavecenter-wavelen/2, wavecenter+wavelen/2+1):
                        pygame.draw.rect(screen, (139, 71, 38),\
                                         (offset_x+i*bar_width,\
                                          offset_y-int(level+waveseq[i-wavecenter+wavelen/2]),\
                                          bar_width,\
                                          int(waveseq[i-wavecenter+wavelen/2])),\
                                         0)
            h, v = self.__intgrt__(h,v)
            pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((800, 600))
Game().main(screen)
