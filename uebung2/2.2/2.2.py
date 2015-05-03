import pygame
from time import clock
from math import pi,sin,cos,sqrt

dt = 0.01
g = 98

class Game(object):
	
	def __init__(self):
		pass

	def __func1__(self, t1, t2, o1, o2):
		l01 = self.arm_length01
		l12 = self.arm_length12
		m1 = self.mess1
		m2 = self.mess2
		a = (g/l01)*(sin(t2)*cos(t1-t2)-(1+(m1/m2))*sin(t1))-o2**2*(l12/l01)*sin(t1-t2)-o1**2*sin(t1-t2)*cos(t1-t2)
		b = 1+(m1/m2)-cos(t1-t2)**2
		return a/b

	def __func2__(self, t1, t2, o1, o2, oa1):
		l01 = self.arm_length01
		l12 = self.arm_length12
		m1 = self.mess1
		m2 = self.mess2
		return -oa1*(l01/l12)*cos(t1-t2)+o1**2*(l01/l12)*sin(t1-t2)-(g/l12)*sin(t2)


	def __intg__(self, theta1, theta2, omega1, omega2):
		o1 = omega1+dt*self.__func1__(theta1, theta2, omega1, omega2)
		o2 = omega2+dt*self.__func2__(theta1, theta2, omega1, omega2, (o1-omega1)/dt)
		t1 = theta1+dt*o1
		t2 = theta2+dt*o2
		return (t1, t2, o1, o2)

	def main(self, screen):

		x_scale, y_scale = screen.get_size()
		
		theta10 = (-45.0/180.0)*pi
		theta20 = (-30.0/180.0)*pi
		omega10 = 0.0
		omega20 = 0.0
		self.arm_length01 = 100.0
		self.arm_length12 = 100.0
		self.mess1 = 100.0
		self.mess2 = 100.0
		nail_offset_y = 100
		nail_offset_x = x_scale/2.0
		
		theta1 = theta10
		theta2 = theta20
		omega1 = omega10
		omega2 = omega20
		
		image = pygame.image.load("ball.png")
		image_scale_1x = 21
		image_scale_1y = 21
		image_scale_2x = 21
		image_scale_2y = 21

		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and\
					event.key == pygame.K_ESCAPE:
					return


			screen.fill((200,200,200))


			p1x, p1y = (int(nail_offset_x+self.arm_length01*sin(theta1)),
						int(nail_offset_y+self.arm_length01*cos(theta1)))
			image_pos_1x, image_pos_1y = (p1x-image_scale_1x/2,
										p1y-image_scale_1y/2)
			screen.blit(image, (image_pos_1x, image_pos_1y))
			pygame.draw.aaline(screen, (10,10,10), 
							(nail_offset_x, nail_offset_y), (p1x, p1y))

			p2x, p2y = (int(p1x+self.arm_length12*sin(theta2)),
						int(p1y+self.arm_length12*cos(theta2)))
			image_pos_2x, image_pos_2y = (p2x-image_scale_2x/2,
										p2y-image_scale_2y/2)
			screen.blit(image, (image_pos_2x, image_pos_2y))
			pygame.draw.aaline(screen, (10,10,10),
							(p1x, p1y), (p2x, p2y))

			
			pygame.display.flip()
			
			
			theta1, theta2, omega1, omega2 = self.__intg__(theta1, theta2, omega1, omega2)
			
			
if __name__ == '__main__':
	pygame.init()

	screen = pygame.display.set_mode((801, 601))
	Game().main(screen)
