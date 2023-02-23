def luhn(bin):
	sum=0
	cc=len(bin)
	agregar=cc&1
	for i in range(0,cc):
		num=int(bin[i])
		if not ((i&i)^agregar):
			num=num*2
		if num >9:
			num=num-9
		sum=sum+num
	return((sum%10)==0)
		

from random import randint as ran
def generador(card):
		bins=""
		if len(card) == 16:
			for i in range(16):
				if card[i] in ("0","1","2","3","4","5","6","7","8","9"):
					bins=bins+card[i]
				elif card[i] in ("x"):
					bins=bins+str(ran(0,9))
				elif card[i] in (""):
					bins=bins+str(ran(0,9))
			for i in range(10):
				check=bins[:15]
				check=check+str(i)
				if luhn(check):
					bins=check
				else:
					check=bins
		return(bins)
		
def fecha(mes,año):
	if mes == "" and año == "":
		mes=str(ran(1,12))
		año=str(ran(23,30))
		if len(mes)<2:
			mes="0"+str(ran(1,9))
		else:
			pass
	elif mes != "" or año != "":
		mes=mes+str(ran(1,12))
		if len(mes)<2:
			mes="0"+str(ran(1,9))
		else:
			pass
			
	return(mes+"|"+año)
	
def cvv(cvc):
	if cvc:
		pass
	else:
		codigo=ran(10,999)
		if codigo<100:
			
			cvc="0"+str(codigo)
		else:
			cvc=str(codigo)
	return("|"+cvc)
	
	