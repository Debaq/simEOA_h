import pygame
from pygame.locals import *
import lib
import time
import os #esto para imprimir, se debe instalar la impresora

#>>> os.system("lp -d thermal -o cpi=12 -o lpi=8 qr.png")


r =[['BAD','BAD',1,1],
    ['OK','OK',1,1],
    ['NOISE','NOISE',1,1],
    ['B','A'],
    ['PLUS','MINUS']]

obr = [['EMPTY','EMPTY',1,1],
    ['EMPTY','EMPTY',1,1],
    ['EMPTY','EMPTY',1,1],
    ['EMPTY','EMPTY'],
    ['EMPTY','EMPTY']]


menu =    [ [0,1],
            [0,1],
            [0,1],
            [0],
            [0,1],
            [0,1],
            [0,1],
            [0,1],
            [0,1]]

pos_row = [0,5,10,40,70,115]
pos_col_prop = [0,5,15,50,80,115,150,180,215,250,280]
pos_col = [pos_col_prop[0],pos_col_prop[1],pos_col_prop[2],
            pos_col_prop[3],pos_col_prop[4],pos_col_prop[5],
            pos_col_prop[6],pos_col_prop[7],pos_col_prop[8],
            pos_col_prop[9],pos_col_prop[10]]

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
        self.test = [False,[]]
        pbar = ['pbar_0','pbar_13','pbar_23','pbar_50','pbar_65','pbar_80','pbar_100']
        self.eoa = lib.animate(pbar)

        self.r = r
        result_dp_OD, result_dp_OI= lib.resultados(OD=self.r[0][0],OI=self.r[0][1])
        result_tr_OD, result_tr_OI= lib.resultados(OD=self.r[1][0],OI=self.r[1][1])
        result_peatc_OD, result_peatc_OI= lib.resultados(OD=self.r[2][0],OI=self.r[2][1])


        self.blites_seccion1=[['lbl_EOADP', pos_row[1], pos_col[2]],
                    ['lbl_EOADP_quick',pos_row[5], pos_col[2]],
                    [self.result('eoa',eoa='dp')[0][0], pos_row[3], pos_col[3]],
                    [self.result('eoa',eoa='dp')[1][0], pos_row[3], pos_col[4]],
                    [self.result('eoa',eoa='dp')[0][1], pos_row[4], pos_col[3]],
                    [self.result('eoa',eoa='dp')[1][1], pos_row[4], pos_col[4]],
                    ['lbl_right', pos_row[2], pos_col[3]],
                    ['lbl_left', pos_row[2], pos_col[4]]]

        self.blites_seccion2=[['lbl_PEATC',pos_row[1], pos_col[5]],
                    ['lbl_PEATC_quick',pos_row[5], pos_col[5]],
                    [result_peatc_OD[0], pos_row[3], pos_col[6]],
                    [result_peatc_OI[0], pos_row[3], pos_col[7]], 
                    [result_peatc_OD[1], pos_row[4], pos_col[6]],
                    [result_peatc_OI[1], pos_row[4], pos_col[7]],
                    ['lbl_right', pos_row[2], pos_col[6]],
                    ['lbl_left', pos_row[2], pos_col[7]]]

        self.blites_seccion3=[['lbl_TIMP',pos_row[1], pos_col[8]],
                    ['lbl_TIMP_226',pos_row[5], pos_col[8]],
                    [self.result('Z',frecuency='226')[0][0], pos_row[3], pos_col[9]],
                    [self.result('Z',frecuency='226')[1][0], pos_row[3], pos_col[10]],
                    [self.result('Z',frecuency='226')[0][1], pos_row[4], pos_col[9]],
                    [self.result('Z',frecuency='226')[1][1], pos_row[4], pos_col[10]],
                    ['lbl_right', pos_row[2], pos_col[9]],
                    ['lbl_left', pos_row[2], pos_col[10]]]
# ---------------------------------------------------------------------
    def result(self, test, frecuency = '226', eoa='dp'):
        if test == 'Z':
            if frecuency == '226':
                result_Z = lib.resultados(OD=self.r[3][0],OI=self.r[3][1])
                return result_Z
            if frecuency == '1000':    
                result_Z = lib.resultados(OD=self.r[4][0],OI=self.r[4][1])
                return result_Z
        if test == 'eoa':
            if eoa == 'dp':
                result_EOA = lib.resultados(OD=self.r[0][0],OI=self.r[0][1])
                return result_EOA
            if eoa == 'tr':
                result_EOA = lib.resultados(OD=self.r[1][0],OI=self.r[1][1])
                return result_EOA

    def loop(self):
        # Loop de pygame
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                   return
                if event.type == pygame.KEYDOWN:
                    if self.test[0] == False:
                        if event.key == pygame.K_UP:
                            self.pos_cursor.prev_row()
                        if event.key == pygame.K_DOWN:
                            self.pos_cursor.next_row()
                        if event.key == pygame.K_RIGHT:
                            self.pos_cursor.next_col()
                        if event.key == pygame.K_LEFT:
                            self.pos_cursor.prev_col()
                        if event.key == pygame.K_RETURN:
                            no_entry = [0,3,6]
                            if self.pos_cursor.now()[1][0] not in no_entry:
                                self.test[0] = True
                            print(self.pos_cursor.now())
                    if event.key == pygame.K_ESCAPE:
                        self.test[0] = False
                    if event.key == pygame.K_a:
                        self.anim()

            self.main()
            pygame.display.flip()

    def blit(self, name, x,y):
        self.screen.blit(self.img[name],(x,y))

    def main(self):
        if self.test[0]:
            seccion = self.pos_cursor.now()
            seccion_eoa = [1,2]
            seccion_abr = [4,5]
            seccion_Z = [7,8]
            self.blit('background2',0,0)
            if seccion[1][0] in seccion_eoa:
                if seccion[0][0][1][0] == 0:
                    self.test_DP()
                if seccion[0][0][1][0] == 1:
                    self.test_TR()
            if seccion[1][0] in seccion_abr:
                self.test_ABR()
            if seccion[1][0] in seccion_Z:
                self.test_Z()                

        else:
            self.blit('background1',0,0)
            self.seccion_1()
            self.seccion_2()
            self.seccion_3()
            self.select()

    def select(self):
        select=self.pos_cursor.now()
        i = select[1][0]
        d = select[0][i]

        self.lista_select1=[
        ['lbl_EOADP_s', pos_row[1], pos_col[2]],
        ['lbl_right_s', pos_row[2], pos_col[3]],
        ['lbl_left_s', pos_row[2], pos_col[4]],
        ['lbl_PEATC_s',pos_row[1], pos_col[5]],
        ['lbl_right_s', pos_row[2], pos_col[6]],
        ['lbl_left_s', pos_row[2], pos_col[7]],
        ['lbl_TIMP_s',pos_row[1], pos_col[8]],
        ['lbl_right_s', pos_row[2], pos_col[9]],
        ['lbl_left_s', pos_row[2], pos_col[10]]]
        #Seccion 1
        if select[0][0][1][0] == 0:
            lbl_eoa_s = 'lbl_EOADP_s'
            lbl_eoa = 'lbl_EOADP'
            lbl_eoa_quick = 'lbl_EOADP_quick'
            type_eoa = 'dp'
        if select[0][0][1][0] == 1:
            lbl_eoa_s = 'lbl_EOATR_s'
            lbl_eoa = 'lbl_EOATR'
            lbl_eoa_quick = 'lbl_EOATR_quick'
            type_eoa = 'tr'

        self.lista_select1[0][0] = lbl_eoa_s
        self.blites_seccion1[0][0] = lbl_eoa
        self.blites_seccion1[1][0] = lbl_eoa_quick
        self.blites_seccion1[2][0] = self.result('eoa',eoa=type_eoa)[0][0]
        self.blites_seccion1[3][0] = self.result('eoa',eoa=type_eoa)[1][0]
        self.blites_seccion1[4][0] = self.result('eoa',eoa=type_eoa)[0][1]
        self.blites_seccion1[5][0] = self.result('eoa',eoa=type_eoa)[1][1]
        #seccion 2

        #Seccion 3
        if select[0][6][1][0] == 0:
            lbl_Z = 'lbl_TIMP_226'
            frecuency = '226'
        if select[0][6][1][0] == 1:
            lbl_Z = 'lbl_TIMP_1000'
            frecuency = '1000'

        self.blites_seccion3[1][0] = lbl_Z
        self.blites_seccion3[2][0] = self.result('Z',frecuency=frecuency)[0][0]
        self.blites_seccion3[3][0] = self.result('Z',frecuency=frecuency)[1][0]
        self.blites_seccion3[4][0] = self.result('Z',frecuency=frecuency)[0][1]
        self.blites_seccion3[5][0] = self.result('Z',frecuency=frecuency)[1][1]
                
        if d[1][0] == 0:
            self.blit(self.lista_select1[i][0],self.lista_select1[i][1],self.lista_select1[i][2])
        if d[1][0] !=0:
            self.blit(self.lista_select1[i][0],self.lista_select1[i][1],self.lista_select1[i][2])

    def seccion_1(self):
        for i in range(len(self.blites_seccion1)):
            self.blit(self.blites_seccion1[i][0],self.blites_seccion1[i][1],self.blites_seccion1[i][2])

    def seccion_2(self):
        for i in range(len(self.blites_seccion2)):
            self.blit(self.blites_seccion2[i][0],self.blites_seccion2[i][1],self.blites_seccion2[i][2])

    def seccion_3(self):
        for i in range(len(self.blites_seccion3)):
            self.blit(self.blites_seccion3[i][0],self.blites_seccion3[i][1],self.blites_seccion3[i][2])

    def test_DP(self):
        select = self.pos_cursor.now()
        lado = select[1][0]
        if  lado == 1:
            print("DP-OD")
        if  lado == 2:
            print("DP-OI")
    def test_TR(self):
        select = self.pos_cursor.now()
        lado = select[1][0]
        if  lado == 1:
            self.blit('lbl_right',200,5)
            self.anim()
        if  lado == 2:
            self.blit('lbl_left',200,5)
            self.anim()
            
    def test_ABR(self):
        select = self.pos_cursor.now()
        lado = select[1][0]
        if  lado == 4:
            print("ABR-OD")
        if  lado == 5:
            print("ABR-OI")

    def test_Z(self):
        select = self.pos_cursor.now()
        lado = select[1][0]
        
        if  lado == 7:
            print("DP-OD")
        if  lado == 8:
            print("DP-OI")

    def anim(self):
        stop = self.eoa.stop
        if stop == False:
            time.sleep(.5)
            self.eoa.animated(tick=100)
            name = self.eoa.name
            self.blit(self.blites_seccion1[0][0],65,40)
            self.blit('lbl_progreso',15,82)
            self.blit(name,110,80)
        if stop == True:
            time.sleep(2)
            self.test[0] = False

        

if __name__ == '__main__':
    a = portatil()
    a.loop()