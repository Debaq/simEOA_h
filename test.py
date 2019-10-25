#!/usr/bin/python

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


