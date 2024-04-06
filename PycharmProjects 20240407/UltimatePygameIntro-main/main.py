import pygame as pg
import sys
BACKGROUND_COLOR = "#B1DDC6"

pg.init()
screen = pg.display.set_mode((800, 400))
pg.display.set_caption('Flasher')
clock = pg.time.Clock()

sky_image = pg.image.load('graphics/Sky.png')
ground_image = pg.image.load('graphics/ground.png')
text_font = pg.font.Font(None, 50)
text_surface = text_font.render(('My game', False, color))
# anus.fill('Red')

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT: pg.quit(); sys.exit()
    screen.blit(sky_image,(0,0))
    screen.blit(ground_image, (0,300))
    pg.display.update()
    clock.tick(60)



