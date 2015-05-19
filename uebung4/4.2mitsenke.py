import pygame
from time import clock
from math import sin, cos, pi, log, e

dom_len = 10
temp_len = 80 
grid_len = 5

offset_x = 200
offset_y = 100

delta_t = 0.01
tempspeed = 8.0
delta_x = float(dom_len)/float(temp_len)

dirc = ((-1,0),(1,0),(0,1),(0,-1))

palette = [(p, 0, 255-p) for p in range(256)]

env_temp = -11.0

class Game(object):
    def __intgrt__(self, temp, v):
       
        for i in range(1, temp_len+1):
            temp[0][i] = temp[1][i]
            temp[i][0] = temp[i][1]
            temp[temp_len+1][i] = temp[temp_len][i]
            temp[i][temp_len+1] = temp[i][temp_len]
        temp[temp_len/2][0] = -11.0
        
        for i in range(1, temp_len+1):
            for j in range(1, temp_len+1):
                t = 0
                for k in range(len(dirc)):
                    t = t+temp[i+dirc[k][0]][j+dirc[k][1]]
                t = t - 4*temp[i][j]
                v[i][j] = v[i][j]+(delta_t*tempspeed**2/delta_x**2)*t
        
        for i in range(1, temp_len+1):
            for j in range(1, temp_len+1):
                t = temp[i][j]+delta_t*v[i][j]
                temp[i][j] = t if t>=env_temp else env_temp
        return temp, v
     
    def main(self, screen):
        x_scale, y_scals = screen.get_size()
        temp = [([0.0]*(temp_len+2)) for i in range(temp_len+2)]
        v = [([0.0]*(temp_len+2)) for i in range(temp_len+2)]
        for i in range(1, temp_len+1):
            x = float(i)*delta_x
            for j in range(1, temp_len+1):
                y = float(j)*delta_x
                temp[i][j] = sin(x)+x*cos(y)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and\
                    event.key == pygame.K_ESCAPE:
                    return
                
            screen.fill((200, 200, 200))
            for i in range(1, temp_len+1):
                for j in range(1, temp_len+1):
                    try:
                        pygame.draw.rect(screen, palette[int((temp[i][j]+11.0)/22.0*255)],\
                                     (offset_x+(i-1)*grid_len,\
                                      offset_y+(j-1)*grid_len,\
                                      grid_len,\
                                      grid_len),\
                                     0)
                    except Exception, e:
                        print '(',i,',',j,')',':',temp[i][j]
                        print e
                        return 1
            temp, v = self.__intgrt__(temp,v)
            pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((800, 600))
Game().main(screen)
