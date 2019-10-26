#!/usr/bin/python
import fnmatch
import os
import pygame
import time



def resultados(OD='EMPTY', OI='EMPTY'):

    lista=['EMPTY','OK','BAD', 'NOISE']

    if OD and OI in lista:

        def code(oi):
            if oi == 'EMPTY':
                oi = 0
            if oi == 'OK':
                oi = 1
            if oi == 'BAD':
                oi = 2
            if oi == 'NOISE':
                oi = 3
            if oi== 'A':
                oi = 4
            if oi== 'B':
                oi = 5
            if oi== 'C':
                oi = 6
            if oi== 'PLUS':
                oi = 7
            if oi== 'MINUS':
                oi = 8
            return oi

    
        OD_c=code(OD)
        OI_c=code(OI)
    
        check = ['check_empty','check_ok','check_error','check_dude','check_a','check_b','check_c','check_plus','check_minus']
        lbl = ['lbl_nodata','lbl_pasa','lbl_refiere','lbl_ruidoso','lbl_TIMP_data','lbl_TIMP_data','lbl_TIMP_data','lbl_TIMP_data']
        
        OD = [check[OD_c],lbl[OD_c]]
        OI = [check[OI_c],lbl[OI_c]]
        
        result = OD,OI
        return result

    else:
        raise NameError('Error de estado, solo usar:' , lista)

def load_image(filename, transparent=False):
        image = pygame.image.load(filename)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


def cargar_img(dir='.', ext='png'):

    lista = {}

    for file in os.listdir('img'):
        if fnmatch.fnmatch(file, '*.'+ext):
            name = file.split('.')
            lista[name[0]]=load_image(dir+'/'+file)
       
    return lista

class animate():
    """Clase para animar con un tiempo determinado entre cuadros"""
    def __init__(self,lista):
        self.lista = lista
        self.len_lista = len(self.lista)
        self.cursor = -1
        self.init_time = self.clock()
        self.stop = False
        self.name = self.lista[0]
        self.configure()

    def configure(self, tick=10, last_time=0):
        self.ticks = tick
        self.last_time=last_time

    def clock(self):
        current_time = pygame.time.get_ticks()
        return current_time

    def iterar(self):
        self.cursor = self.cursor + 1
        self.animar(self.cursor)

    def animar(self,n):
        self.name = (self.lista[n])
        if self.cursor+1 == self.len_lista:
            self.stop = True

    def animated(self, tick):
        if self.last_time == 0:
            last_time=self.init_time
        else:
            last_time = self.last_time
        time=self.ticks
        current_time = self.clock()

        if current_time > last_time:
            self.last_time = current_time + self.ticks
            self.iterar()

        self.configure(tick, last_time=self.last_time)


class change_state():
    def __init__(self, quantity=2, matrix=0):
        if isinstance(matrix, list) == False:
            self.quantity = quantity
            self.lista = range(self.quantity) 
            self.lista=list(self.lista)

        if isinstance(matrix, list) == True:
            self.lista=[[],[0]]
            for i in matrix:
                self.lista[0].append([i,[0]])

        self.cursor_row = self.lista[0][self.lista[1][0]]
        self.cursor_col=self.cursor_row[0][self.cursor_row[1][0]]


               
    def now(self):
#        self.cursor_col=self.cursor_row[0][self.cursor_row[1][0]]
 #       d = ("row: ",self.cursor_row, "col: ",self.cursor_col)         
        return self.lista

    def next_row(self):
        full=(len(self.lista[0])-1)
        if self.lista[1][0] >= 0:
            self.lista[1][0] += 1
        if self.lista[1][0] >full:
            self.lista[1][0] = 0 
        index = self.lista[1][0]
        self.cursor_row=self.lista[0][index]

    def prev_row(self):
        full=(len(self.lista[0])-1)
        if self.lista[1][0] < 0:
            self.lista[1][0] = full
        if self.lista[1][0] <=full:
            self.lista[1][0] -= 1
        index = self.lista[1][0]
        self.cursor_row=self.lista[0][index]

    def next_col(self):
        full=(len(self.cursor_row[0])-1)
        if self.cursor_row[1][0] >= 0:
            self.cursor_row[1][0] += 1
        if self.cursor_row[1][0] >full:
            self.cursor_row[1][0] = 0 
        index = self.cursor_row[1][0]
        self.cursor_col=self.cursor_row[0][index]
    def prev_col(self):
        full=(len(self.cursor_row[0])-1)
        if self.cursor_row[1][0] < 0:
            self.cursor_row[1][0] = full
        if self.cursor_row[1][0] <=full:
            self.cursor_row[1][0] -= 1
        index = self.cursor_row[1][0]
        self.cursor_col=self.cursor_row[0][index]