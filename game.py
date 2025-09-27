import pygame as pg  
from sys import exit

pg.init() 

class Bro(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = [pg.image.load('graphics/Player/player_walk_1.png').convert_alpha(),
                       pg.image.load('graphics/Player/player_walk_2.png').convert_alpha()]
        self.bro_jump = pg.image.load('graphics/Player/jump.png').convert_alpha()
        self.jumping = False
        self.index = 0
        self.gravity = 1
        self.velocity = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom=(50, 300))

    def jump(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.rect.bottom == 300:
            self.velocity = -20
            self.jumping = True
        if self.jumping:
            self.rect.bottom += self.velocity
            self.velocity += self.gravity
            self.image = self.bro_jump
        if self.rect.bottom > 300:
            self.rect.bottom = 300
            self.velocity = 0
            self.jumping = False

    def animate(self):
        self.index += 0.1
        if self.index > len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self):
        self.animate()
        self.jump()


size = WIDTH, HEIGHT = 800, 400

screen = pg.display.set_mode(size)

icon = pg.image.load('graphics/icon.png').convert_alpha()
sky = pg.image.load('graphics/sky.png').convert()
ground = pg.image.load('graphics/ground.png').convert()
snail = [
	pg.image.load('graphics/snail/snail1.png').convert_alpha(),
	pg.image.load('graphics/snail/snail2.png').convert_alpha()
]
fly = [
	pg.image.load('graphics/Fly/Fly1.png').convert_alpha(),
	pg.image.load('graphics/Fly/Fly2.png').convert_alpha()
]

bro_stand = pg.image.load('graphics/Player/player_stand.png').convert_alpha()

pg.display.set_caption("Jumper Bro")
pg.display.set_icon(icon)

bro = pg.sprite.GroupSingle()
bro.add(Bro())

fps = 60
clock = pg.time.Clock()

while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			exit()

	screen.blit(sky,(0,0))
	screen.blit(ground,(0, 300))

	bro.update()
	bro.draw(screen)

	pg.display.update()
	clock.tick(fps)

		