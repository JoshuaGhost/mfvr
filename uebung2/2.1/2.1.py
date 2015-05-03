import pygame
from time import clock
from math import pi,sin,cos,sqrt

dt = 0.001

class Game(object):
	
	def __init__(self):
		pass

	def __intg__(self, p0, v0, a):
		v1 = a*dt+v0
		p1 = v1*dt+p0
		return (p1, v1)

	def __gety__(self, x):
		return sqrt(self.sqr_arm_length-x**2)-self.yf

	def main(self, screen):

		x_scale, y_scale = screen.get_size()
		
		theta0 = (45.0/180.0)*pi
		arm_length = 200.0
		nailoffsety = 100
		x_offset = x_scale/2.0
		y_offset = nailoffsety+arm_length * cos(theta0)
		nailpointx = x_offset
		nailpointy = nailoffsety
		k = 2
		px = arm_length*sin(theta0)
		py = 0
		vx = 0
		vy = 0
		ax = -k*px
		
		self.yf = sqrt(arm_length**2-px**2)
		self.sqr_arm_length = arm_length**2

		image = pygame.image.load("ball.png")
		
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and\
					event.key == pygame.K_ESCAPE:
					return
				if event.type == pygame.KEYDOWN and\
					event.key == pygame.K_DOWN and\
					k > 40:
					k = k - 20
				if event.type == pygame.KEYDOWN and\
					event.key == pygame.K_UP: #and k < 1000:
					k = k * 10
			screen.fill((200,200,200))
			imageposx = int(px+x_offset-10)
			imageposy = int(py+y_offset-10)
			pygame.draw.aaline(screen, (10,10,10), 
								(nailpointx, nailpointy),
								(int(px+x_offset), int(py+y_offset)))

			screen.blit(image, (imageposx, imageposy))
			pygame.display.flip()
			
			px,vx = self.__intg__(px, vx, ax)
			ax = -px*k
			py = self.__gety__(px)
			
if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((801, 601))
	Game().main(screen)