import getopt,sys
from random import randint as r
import datetime
import time
import os
#Esta funcion imprime el menu en consola con las opciones 
def menu():
	print(time.ctime(),'-> hello, my name is xela-stone')
	baner='''
		este es un menu informativo
		
		seleccione los siguentes comandos
		-h para imprimir el mensaje de ayuda
		-b para introducir el formato bin
		-l la cantidad de bins a generar
		-c para generar el cvv aleatorio
		-f para generar la fecha aleatoriamente
		-d para checar la procedencia del bin
	
	ejemplo python3 get.py -b 123456789xxxxxxx -l 666 -d -f
	
	
	'''
	print(baner)
	
#Esta es una funcion de análisis de opcion de linea de comandos 
def met(argv):
	cvv=False
	fecha=False
	bincc=''
	limite=10
	#dat=False
	#argv=sys.argv[1:]
	tom,args=getopt.getopt(argv,'hb:l:cf',['ayuda','bin','limite','dato','fecha'])
	for x,y in tom:
		if x in ('-h'):
			menu()
			sys.exit()
		elif x in ('-b','bin'):
			bincc=y
			#print(bincc)

		elif x in ('-l','limite'):
			limite=y
			#print(var)
		#return(var,bool)
		elif x in ('-c','cvv'):
			cvv=True
		elif x in ('-f','fecha'):
			fecha=True
		
	return(bincc,limite,cvv,fecha)

#Es un verificador que detecta el error de unico dígito 
def luhn(num):
	#num='42131661'
	sum=0
	cc=len(num)
	add=cc&1
	for i in range(0,cc):
		digito=int(num[i])
		if not ((i&i)^add):
			digito=digito*2
		if digito >9:
			digito=digito-9
		sum=sum+digito
	return((sum%10)==0)
#luhn()

#Es el generador de los 16 numero de la tarjeta de crédito 
#No genera tarjetas amex solo master y visa
def generador(bincc):
#	bincc=input('')
	cc=''
	if len(bincc) == 16:
		for i in range(16):
			if bincc[i] in ('0','1','2','3','4','5','6','7','8','9'):
				cc=cc+bincc[i]
			elif bincc[i] in ('x'):
				cc=cc+str(r(0,9))

		for s in range(10):
			check=cc
			check=check+str(s)
			if luhn(check):
				if len(check) == 16:

					cc=check
					break
			else:
				if len(check) == 16:
					check=cc
				#print(cc)
	return(cc)
#generador()
#Esta funcion genera el cvv aleatorio de 3 digitos.
def seguridad():
	cvv=''
	var=r(10,999)
	if var <100:
		cvv='0'+str(var)
	else:
		cvv=str(var)
	return(cvv)

#En esta función generamos la fecha y año de las tarjtas	
def dato():
	tiempo=datetime.datetime.now()
	dato=''
	mes=str(r(1,12))
	if len(mes) != 2:
		mes='0'+mes
	cont=str(tiempo.year)
	anio=str(r(int(cont[-2:])+1,int(cont[-2:])+6))
	dato=mes+'|'+anio
	return(dato)
#fecha()
#Esta es la funcion principal 
def main(argv):
	lista=[]
	(bincc,limite,cvv,fecha)=met(argv)
	if bincc != '':
		for i in range(int(limite)):
			#print(bincc)
			#lista.append(generador(bincc))
			#print(lista[i])

			if cvv and fecha:
				lista.append(generador(bincc)+ '|' +seguridad()+ '|' +dato())
				print(lista[i])
			elif cvv and not fecha:
				lista.append(generador(bincc)+ '|' +seguridad())
				print(lista[i])
				
			elif fecha and not cvv:
				lista.append(generador(bincc)+ '|' + dato())
				print(lista[i])
	#		elif dat:
	#			os.system('python3 loop_list.py')	
	#			sys.exit(3)
#	pass
if __name__=='__main__':

	main(sys.argv[1:])
