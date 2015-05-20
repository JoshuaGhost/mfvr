import pygame
from time import clock
from math import sin, cos, pi, log, e

dom_len = 1
map_len = 100 
grid_len = 3

offset_x = 100
offset_y = 100

delta_t = 0.01

class Game(object):

    def __get_v__(self, x, y):
        return sin(x)+cos(y), (x**2*y**3/2-y/(x**2+3))

    def __intgrt__(self, posx, posy):
       
        for i in range(map_len):
            for j in range(map_len):
                vx, vy = self.__get_v__(posx[i][j], posy[i][j])
                posx[i][j] = posx[i][j] + delta_t * vx
                posy[i][j] = posy[i][j] + delta_t * vy

        return posx, posy

    def main(self, screen):
        x_scale, y_scals = screen.get_size()
        color = [([0] * map_len) for i in range(map_len)]
        posx = [([0] * map_len) for i in range(map_len)]
        posy = [([0] * map_len) for i in range(map_len)]
        for i in range(map_len):
            for j in range(map_len):
                x = float(i)/float(map_len)
                y = float(j)/float(map_len)
                color[i][j] = (int(float(i+j)/float(i+1)/map_len * 255), 
                               int(((sin(i)+sin(j))/2+1)/2 * 255),
                               int(float(i-j)**2 / map_len**2 * 255))
                posx[i][j] = x
                posy[i][j] = y
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and\
                    event.key == pygame.K_ESCAPE:
                    return
                
            screen.fill((200, 200, 200))
            for i in range(map_len):
                for j in range(map_len):
                    try:
                        pygame.draw.rect(screen, color[i][j],\
                                    (offset_x+int(posx[i][j]*float(map_len))*grid_len,\
                                    offset_y+int(posy[i][j]*float(map_len))*grid_len,\
                                      3,\
                                      3),\
                                     0)
                    except Exception, e:
                        posx[i][j] = 0
                        posy[i][j] = 0
                        color[i][j] = (200,200,200)
#                        print e
#return 1
            posx, posy = self.__intgrt__(posx, posy)
            pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((800, 600))
Game().main(screen)
