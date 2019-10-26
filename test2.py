

import pygame
from pygame.locals import *
import lib


# ---------------------------------------------------------------------

class gui():
    
    def __init__(self):
        self.main()

    def main(self):
        pygame.mouse.set_visible(0)
        size=width, height = 240,320
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("EOA-PEATC-Z")

        pygame.display.flip()

        img = lib.cargar_img(dir='img') #se cargan todas las imagenes
        pbar = ['pbar_13','pbar_23','pbar_50','pbar_65','pbar_80','pbar_100']
        a = lib.animate(pbar)
        fin = False

        # Loop de pygame
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            if fin == False:
                a.animated(tick=1000)
                fin = a.stop
                name = a.name
                self.screen.blit(img[name],(0,0))
                pygame.display.flip()


 

if __name__ == '__main__':
    pygame.init()
    gui()






