import pygame as pg  
from sys import exit

pg.init() 

size = WIDTH, HEIGHT = 800, 400

screen = pg.display.set_mode(size)
pg.display.set_caption("Jumper Bro")

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			exit()


		