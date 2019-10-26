import pygame
from pygame.locals import *
import lib


r =[['BAD','BAD',1,1],
    ['BAD','BAD',1,1],
    ['BAD','BAD',1,1],
    ['B','B']]

menu =    [[0,1],
            [0,1,2],
            [0,1,2],
            [0],
            [0,1,2],
            [0,1,2],
            [0,1],
            [0,1,2],
            [0,1,2]]

pos_row = [0,5,10,40,70,115]
pos_col = [0,5,15,50,80,115,150,180,215,250,280]

class portatil():
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(0)
        size=width, height = 240,320
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("EOA-PEATC-Z")
        pygame.display.flip()
        self.img = lib.cargar_img(dir='img') #se cargan todas las imagenes
        self.pos_cursor = lib.change_state(matrix = menu)
        self.test = False
    # ---------------------------------------------------------------------
    def loop(self):
        # Loop de pygame
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                   return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.pos_cursor.prev_row()
                    if event.key == pygame.K_DOWN:
                        self.pos_cursor.next_row()
                    if event.key == pygame.K_RIGHT:
                        self.pos_cursor.next_col()
                    if event.key == pygame.K_LEFT:
                        self.pos_cursor.prev_col()
                    
                    #print(self.pos_cursor.now())

            self.main()
            pygame.display.flip()

    def blit(self, name, x,y):
        self.screen.blit(self.img[name],(x,y))

    def main(self):

        if self.test:
            self.blit('background2',0,0)
        else:
            self.blit('background1',0,0)
            self.lbl()
            self.results_dp()
            self.results_peatc()
            self.results_z_226()
            self.select()

    def select(self):
        select=self.pos_cursor.now()
        i = select[1][0]

        self.lista_select=[
        ['lbl_EOADP_s', pos_row[1], pos_col[2]],
        ('lbl_right_s', pos_row[2], pos_col[3]),
        ('lbl_left_s', pos_row[2], pos_col[4]),
        ('lbl_PEATC_s',pos_row[1], pos_col[5]),
        ('lbl_right_s', pos_row[2], pos_col[6]),
        ('lbl_left_s', pos_row[2], pos_col[7]),
        ('lbl_TIMP_s',pos_row[1], pos_col[8]),
        ('lbl_right_s', pos_row[2], pos_col[9]),
        ('lbl_left_s', pos_row[2], pos_col[10])]

        if select[0][0][1][0] == 1:
            lista_select[0][0] = 'lbl_EOATR_s'


        self.blit(a[i][0],a[i][1],a[i][2])

        #for i in range(len(a)):

         #   self.blit(a[i][0],a[i][1],a[i][2])


    
    def lbl(self):
        self.blit('lbl_right', pos_row[2], pos_col[3])
        self.blit('lbl_left', pos_row[2], pos_col[4])
        self.blit('lbl_right', pos_row[2], pos_col[6])
        self.blit('lbl_left', pos_row[2], pos_col[7])
        self.blit('lbl_right', pos_row[2], pos_col[9])
        self.blit('lbl_left', pos_row[2], pos_col[10])

    def results_tr(self):
        self.blit('lbl_EOATR', pos_row[1], pos_col[2])
        self.blit('lbl_EOATR_quick',pos_row[5], pos_col[2])
        result_tr_OD, result_tr_OI= lib.resultados()
        self.blit(result_tr_OD[0], pos_row[3], pos_col[3])
        self.blit(result_tr_OI[0], pos_row[3], pos_col[4])
        self.blit(result_tr_OD[1], pos_row[4], pos_col[3])
        self.blit(result_tr_OI[1], pos_row[4], pos_col[4])

    def results_dp(self):
        self.blit('lbl_EOADP', pos_row[1], pos_col[2])
        self.blit('lbl_EOADP_quick',pos_row[5], pos_col[2])
        result_dp_OD, result_dp_OI= lib.resultados()
        self.blit(result_dp_OD[0], pos_row[3], pos_col[3])
        self.blit(result_dp_OI[0], pos_row[3], pos_col[4])
        self.blit(result_dp_OD[1], pos_row[4], pos_col[3])
        self.blit(result_dp_OI[1], pos_row[4], pos_col[4])

    def results_peatc(self):
        result_peatc_OD, result_peatc_OI= lib.resultados()
        self.blit('lbl_PEATC',pos_row[1], pos_col[5])
        self.blit('lbl_PEATC_quick',pos_row[5], pos_col[5])
        self.blit(result_peatc_OD[0], pos_row[3], pos_col[6])
        self.blit(result_peatc_OI[0], pos_row[3], pos_col[7])
        self.blit(result_peatc_OD[1], pos_row[4], pos_col[6])
        self.blit(result_peatc_OI[1], pos_row[4], pos_col[7])

    def results_z_226(self):
        result_Z226_OD, result_Z226_OI= lib.resultados()
        self.blit('lbl_TIMP',pos_row[1], pos_col[8])
        self.blit('lbl_TIMP_226',pos_row[5], pos_col[8])
        self.blit(result_Z226_OD[0], pos_row[3], pos_col[9])
        self.blit(result_Z226_OI[0], pos_row[3], pos_col[10])
        self.blit(result_Z226_OD[1], pos_row[4], pos_col[9])
        self.blit(result_Z226_OI[1], pos_row[4], pos_col[10])

    def results_z_1000(self):
        result_Z1000_OD, result_Z1000_OI= lib.resultados(OD='PLUS')
        self.blit('lbl_TIMP',pos_row[1], pos_col[8])
        self.blit('lbl_TIMP_1000',pos_row[5], pos_col[8])
        self.blit(result_Z1000_OD[0], pos_row[3], pos_col[9])
        self.blit(result_Z1000_OI[0], pos_row[3], pos_col[10])
        self.blit(result_Z1000_OD[1], pos_row[4], pos_col[9])
        self.blit(result_Z1000_OI[1], pos_row[4], pos_col[10])
    def eoaTR(self):
        pass

    def eoaDP(self):
        pass

    def autoPEATC(self):
        pass

if __name__ == '__main__':
    a = portatil()
    a.loop()