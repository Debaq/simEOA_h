#!/usr/bin/python
import fnmatch
import os
import pygame

def resultados(OD='OK', OI='OK',r=0):

    lista=['OK','BAD', 'NOISE']

    if OD and OI in lista:

        def code(oi):
            if oi == 'OK':
                oi = 1
            if oi == 'BAD':
                oi = 0
            if oi == 'NOISE':
                oi = 2
            return oi

        if r == 1:
            OD=code(OD)
            OI=code(OI)
        

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


