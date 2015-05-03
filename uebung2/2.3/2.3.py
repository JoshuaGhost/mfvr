import pygame
from time import clock
from math import pi,sin,cos,sqrt

dt = 0.01
G = 66700

class Planet(object):

	def __init__(self, x0, y0, vx0, vy0, mass):
		self.x = x0
		self.y = y0
		self.vx = vx0
		self.vy = vy0
		self.mass = mass

class Game(object):
	
	def __init__(self):
		pass

	def __intg__(self, p1, p2):
		
		if (p1.x - p2.x)**2+(p1.y - p2.y)**2<(11+15)**2:
			p1.vx = -p1.vx
			p1.vy = -p1.vy
			p2.vx = -p2.vx
			p2.vy = -p2.vy
			p1.x = p1.x + p1.vx*dt
			p1.y = p1.y + p1.vy*dt
			p2.x = p2.x + p2.vx*dt
			p2.y = p2.y + p2.vy*dt
			return(p1, p2)
		r_hoch_zwei = (p1.x-p2.x)**2+(p1.y-p2.y)**2
		a12x = G*p1.mass*p2.mass/r_hoch_zwei*((p2.x-p1.x)/sqrt(r_hoch_zwei))/p1.mass
		a21x = -a12x*p1.mass/p2.mass
		a12y = G*p1.mass*p2.mass/r_hoch_zwei*((p2.y-p1.y)/sqrt(r_hoch_zwei))/p2.mass
		a21y = -a12y*p1.mass/p2.mass
		p1.vx = p1.vx + a12x*dt
		p1.x = p1.x + p1.vx*dt
		p1.vy = p1.vy + a12y*dt
		p1.y = p1.y + p1.vy*dt
		p2.vx = p2.vx + a21x*dt
		p2.x = p2.x + p2.vx*dt
		p2.vy = p2.vy + a21y*dt
		p2.y = p2.y + p2.vy*dt
		return (p1, p2)

	def main(self, screen):

		x_scale, y_scale = screen.get_size()

		p1 = Planet(200.0, y_scale/2.0, 0.0, 20.0, 10)
		p2 = Planet(600.0, y_scale/2.0, 0.0, -20.0, 10)
		
		
		image_small = pygame.image.load("ball.png")
		image_small_scale_x = 21
		image_small_scale_y = 21
		image_big   = pygame.image.load("ball.png")
		image_big_scale_x   = 21
		image_big_scale_y   = 21

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and\
					event.key == pygame.K_ESCAPE:
					return


			screen.fill((200,200,200))

			image_small_pos_x, image_small_pos_y = (p1.x-image_small_scale_x/2,
										p1.y-image_small_scale_y/2)
			screen.blit(image_small, (image_small_pos_x, image_small_pos_y))
			
			image_big_pos_x, image_big_pos_y = (p2.x-image_big_scale_x/2,
										p2.y-image_big_scale_y/2)
			screen.blit(image_big, (image_big_pos_x, image_big_pos_y))
			
			pygame.display.flip()
			
			p1, p2 = self.__intg__(p1, p2)
		
if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((800, 600))
	Game().main(screen)
