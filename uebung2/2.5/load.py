import pygame
import json
from time import sleep

class Game(object):
	
	def __init__(self):
		pass

	def main(self, screen):
		offset_x = 683
		offset_y = 1
		
		with open("dumpx.json", "r") as df:
			xs = json.load(df)
		with open("dumpy.json", "r") as df:
			ys = json.load(df)
		assert len(xs) == len(ys)

		while 1:
			for i in range(len(xs)):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						return
					if event.type == pygame.KEYDOWN and\
					event.key == pygame.K_ESCAPE:
						return
				screen.fill((200,200,200))
				for j in range(len(xs[i])):
					try:
						pygame.draw.circle(screen,
										   [0,0,0],
										   [int(xs[i][j])+offset_x, int(ys[i][j])+offset_y],
										   1,
										   0)
					except Exception, e:
						print i, ' ', j, ' ', xs[i][j]

						print (int(xs[i][j])+offset_x, " ", int(ys[i][j])+offset_y)
							
				pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((1366,768))
Game().main(screen)
'''
pygame.draw.rect(screen,
									[0,0,0],
									[int(xs[i][j])+offset_x, int(ys[i][j])+offset_y, 2, 2],
									1)'''