#!/usr/bin/python

import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
from subprocess import *
import lib 


into = sys.argv
try:
    if into[1] == '-pi':
        print("rapsberry pi")
        from pitftgpio import PiTFT_GPIO
        pitft = PiTFT_GPIO()
        os.environ["SDL_FBDEV"] = "/dev/fb1"
        os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
        os.environ["SDL_MOUSEDRV"] = "TSLIB"

    else:
        print(into[1])
except:
    pass

FPS =10
state=[0,0,0]
background_image=[]
label_image=[]
check_image=[]
data={"PD":[],"TR":[],"PEATC":[]}

def load_image(filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
# ---------------------------------------------------------------------
class gui():
    """docstring for gui"""
    def __init__(self):
        self.main()

        
    def main(self):
        pygame.mouse.set_visible(0)
        size=width, height = 240,320
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("EOA-PEATC-Z")

        background_image.append(load_image('img/background1.png'))
        background_image.append(load_image('img/background2.png'))
       
        self.principal()

        while True:
            for eventos in pygame.event.get():
                if eventos.type == pygame.KEYDOWN:
                    i =state
                    if eventos.key == pygame.K_UP:
                        state[0]=i[0]-1
                        if state[0]<=0:
                            state[0]=1
                        print(state[0])
                    if eventos.key == pygame.K_DOWN:
                        state[0]=i[0]+1
                        if state[0]>6:
                            state[0]=6
                        print(state[0])

                    if eventos.key == pygame.K_LEFT:
                        if state[0]==1:
                            state[1]=i[1]-1
                            if state[1]<0:
                                state[1]=0
                            print(state[1])
                        if state[0]==4:
                            state[2]=i[2]-1
                            if state[2]<0:
                                state[2]=0
                            print(state[2])
                    if eventos.key == pygame.K_RIGHT:
                        if state[0]==1:
                            state[1]=i[1]+1
                            if state[1]>1:
                                state[1]=1
                            print(state[1])
                        if state[0]==4:
                            state[2]=i[2]+1
                            if state[2]>1:
                                state[2]=1
                            print(state[2])
                    if eventos.key == pygame.K_RETURN:
                        if state[1]==0:
                            if state[0]==2:
                                self.test("pd", "od")
                            if state[0]==3:
                                self.test("pd", "oI")
                        if state[1]==1:
                            if state[0]==2:
                                self.test("Tr", "od")
                            if state[0]==3:
                                self.test("Tr", "oI")
                        if state[0]==5:
                            self.test("PEATC", "od")
                        if state[0]==6:
                            self.test("PEATC", "oI")
    
                    if state[1]==0:
                        if state[0]==1:
                                self.principal(2)
                        if state[0]==2:
                                self.principal(3)
                        if state[0]==3:
                                self.principal(4)
                        if state[0]==4:
                                self.principal(5)
                        if state[0]==5:
                                self.principal(6)
                        if state[0]==6:
                                self.principal(7)  
                    if state[1]==1:
                        if state[0]==1:
                                self.principal(1,1)
                        if state[0]==2:
                                self.principal(3,1)
                        if state[0]==3:
                                self.principal(4,1)
                        if state[0]==4:
                                self.principal(5,1)
                        if state[0]==5:
                                self.principal(6,1)
                        if state[0]==6:
                                self.principal(7,1) 

                if eventos.type == QUIT:
                    sys.exit(0)
               
            pygame.display.flip()
        return 0


    def test(self, test,lado):
        print(test," ", lado)

    def eoatrans(self):
        pass

    def eoadp(self, state):
        pass

    def peatc(self, state):
        pass

    def state_dif(self, state):
        data = {OD:0, OI:0}
        if state == 0: ##PASS BOTH
            data['OD'], data['OI']= 1,1
        if state == 1: ##NOT PASS OD
            data['OD'], data['OI']= 0,1
        if state == 2: ##NOT PASS OD
            data['OD'], data['OI']= 1,0
        if state == 3: ## REFUSE BOTH
            data['OD'], data['OI']= 2,2
        if state == 4: ## REFUSE OD, PASS OI
            data['OD'], data['OI']= 2,1
        if state == 5: ## REFUSE OD, NOT PASS OI
            data['OD'], data['OI']= 2,0
        if state == 6: ## REFUSE OD, PASS OI
            data['OD'], data['OI']= 2,1            

    def principal(self,selec_v=1,selec_h=0):

        label_image.append(load_image('img/lbl_EOADP.png'))         #0
        label_image.append(load_image('img/lbl_EOADP_s.png'))       #1
        label_image.append(load_image('img/lbl_EOATR.png'))         #2
        label_image.append(load_image('img/lbl_EOATR_s.png'))       #3
        label_image.append(load_image('img/lbl_EOADP_quick.png'))   #4
        label_image.append(load_image('img/lbl_PEATC.png'))         #5
        label_image.append(load_image('img/lbl_PEATC_s.png'))       #6
        label_image.append(load_image('img/lbl_left.png'))          #7
        label_image.append(load_image('img/lbl_left_s.png'))        #8
        label_image.append(load_image('img/lbl_right.png'))         #9
        label_image.append(load_image('img/lbl_right_s.png'))       #10
        if selec_h ==0:
            if selec_v==1:
                self.screen.blit(background_image[0], (0, 0))
                self.screen.blit(label_image[0],(2,5))
                self.screen.blit(label_image[9],(10,45))
                self.screen.blit(label_image[7],(10,95))
                self.screen.blit(label_image[5],(2,155))
                self.screen.blit(label_image[9],(10,195))
                self.screen.blit(label_image[7],(10,245))
                self.result()
            if selec_v==2:
                self.screen.blit(label_image[1],(2,5)) #selecciondo
                self.screen.blit(label_image[9],(10,45)) #selccionado
            if selec_v==3:
                self.screen.blit(label_image[0],(2,5)) #normal
                self.screen.blit(label_image[7],(10,95)) #Seleccionado
                self.screen.blit(label_image[10],(10,45)) #selccionado
            if selec_v==4:
                self.screen.blit(label_image[9],(10,45)) #normal
                self.screen.blit(label_image[8],(10,95)) #Seleccionado
                self.screen.blit(label_image[5],(2,155)) #normal
            if selec_v==5:
                self.screen.blit(label_image[7],(10,95)) 
                self.screen.blit(label_image[6],(2,155)) 
                self.screen.blit(label_image[9],(10,195))
            if selec_v==6:
                self.screen.blit(label_image[5],(2,155)) 
                self.screen.blit(label_image[10],(10,195))
                self.screen.blit(label_image[7],(10,245)) 
            if selec_v==7:
                self.screen.blit(label_image[9],(10,195))
                self.screen.blit(label_image[8],(10,245)) 

        if selec_h ==1:
            if selec_v==1:
                self.screen.blit(background_image[0], (0, 0))
                self.screen.blit(label_image[3],(2,5))
                self.screen.blit(label_image[9],(10,45))
                self.screen.blit(label_image[7],(10,95))
                self.screen.blit(label_image[5],(2,155))
                self.screen.blit(label_image[9],(10,195))
                self.screen.blit(label_image[7],(10,245))
            if selec_v==2:
                self.screen.blit(label_image[1],(2,5)) 
                self.screen.blit(label_image[9],(10,45)) 
            if selec_v==3:
                self.screen.blit(label_image[2],(2,5)) 
                self.screen.blit(label_image[7],(10,95)) 
                self.screen.blit(label_image[10],(10,45)) 
            if selec_v==4:
                self.screen.blit(label_image[9],(10,45)) 
                self.screen.blit(label_image[8],(10,95)) 
                self.screen.blit(label_image[5],(2,155)) 
            if selec_v==5:
                self.screen.blit(label_image[7],(10,95)) 
                self.screen.blit(label_image[6],(2,155)) 
                self.screen.blit(label_image[9],(10,195))
            if selec_v==6:
                self.screen.blit(label_image[5],(2,155)) 
                self.screen.blit(label_image[10],(10,195))
                self.screen.blit(label_image[7],(10,245)) 
            if selec_v==7:
                self.screen.blit(label_image[9],(10,195))
                self.screen.blit(label_image[8],(10,245)) 

    def result(self,test=0,lado=0):
        check_image.append(load_image('img/check_empty.png'))   #0
        check_image.append(load_image('img/check_ok.png'))      #1
        check_image.append(load_image('img/check_dude.png'))    #2
        check_image.append(load_image('img/check_error.png'))   #3
        label_image.append(load_image('img/lbl_nodata.png'))    #4
        self.screen.blit(check_image[0],(40,45))
        self.screen.blit(label_image[11],(70,50))
        self.screen.blit(check_image[0],(40,95))
        self.screen.blit(label_image[11],(70,100))
        self.screen.blit(check_image[0],(40,195))
        self.screen.blit(label_image[11],(70,200))
        self.screen.blit(check_image[0],(40,245))
        self.screen.blit(label_image[11],(70,250))




if __name__ == '__main__':
    pygame.init()
    gui()