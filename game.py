import pygame as pg  
from sys import exit

pg.init() 

size = WIDTH, HEIGHT = 800, 400

screen = pg.display.set_mode(size)

icon = pg.image.load('graphics/icon.png').convert_alpha()
sky = pg.image.load('graphics/sky.png').convert()
ground = pg.image.load('graphics/ground.png').convert()
snail = [
	pg.image.load('graphics/snail/snail1.png').convert_alpha(),
	pg.image.load('graphics/snail/snail2.png').convert_alpha()
]
bro = [
	pg.image.load('graphics/Player/player_stand.png').convert_alpha(),
	pg.image.load('graphics/Player/jump.png').convert_alpha(),
	pg.image.load('graphics/Player/player_walk_1.png').convert_alpha(),
	pg.image.load('graphics/Player/player_walk_2.png').convert_alpha()
	]

pg.display.set_caption("Jumper Bro")
pg.display.set_icon(icon)

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			exit()


		