import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from subprocess import *

if os.uname()[1] == 'raspberrypi':
    from pitftgpio import PiTFT_GPIO
    pitft = PiTFT_GPIO()
    os.environ["SDL_FBDEV"] = "/dev/fb1"
    os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
    os.environ["SDL_MOUSEDRV"] = "TSLIB"


FPS =10
state=[1,0]
def load_image(filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
# ---------------------------------------------------------------------
 
def main():
    pygame.mouse.set_visible(0)
    size=width, height = 240,320
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("EOA-PEATC-Z")

    if state[0]==0:
        background_image = load_image('img/background1.png')
    if state[0]==1:
        background_image = load_image('img/background2.png')


    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        screen.blit(background_image, (0, 0))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()