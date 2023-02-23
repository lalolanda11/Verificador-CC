from tkinter import *
from tkinter import messagebox
import gencc
class Raiz(Tk):
	def __init__(self):
		super().__init__()
	#	self.geometry("300x300")
	#	self.config(bg="gray60",menu=self.menu,width=200,height=200)
		
		def Checker():
		#	self.Credit=gencc.generador(str(self.Bincard.get()))
			if self.Bincard.get() and self.Mescard.get() and self.acard.get() and self.cvv.get():
#			self.Mes=gencc.fecha(str(self.Mescard.get()),str(self.acard.get()))
				self.Credit=gencc.generador(str(self.Bincard.get()))
				self.Mes=str(self.Mescard.get())
				self.año=str(self.acard.get())
				self.cvcard=str(self.cvv.get())
				if len(self.Mes)<2 and len(self.cvcard)<3:
					self.Mes="0"+self.Mes
					self.cvcard="0"+self.cvcard
					
			elif self.Bincard.get() and self.acard.get() and self.Mescard.get() and not self.cvv.get()  :
				self.Mes=str(self.Mescard.get())
				self.Credit=gencc.generador(str(self.Bincard.get()))
				self.año=str(self.acard.get())
				self.cvcard=str(gencc.ran(10,999))
				if len(self.Mes)<2 and len(self.cvcard)<3 and len(self.año)<2:
					self.Mes="0"+self.Mes
					self.año=str(gencc.ran(23,30))
					self.cvcard="0"+str(gencc.ran(1,9))
			
			elif self.Bincard.get() and self.acard.get() and self.cvv.get() and not self.Mescard.get():
				self.Credit=gencc.generador(str(self.Bincard.get()))
				self.año=str(self.acard.get())
				self.cvcard=str(self.cvv.get())
				self.Mes=str(gencc.ran(1,12))
				if len(self.Mes)<2:
					self.Mes="0"+self.Mes
#				self.año=self.año
			elif self.Bincard.get() and self.Mescard.get() and self.cvv.get() and not self.acard.get():
				self.Credit=gencc.generador(str(self.Bincard.get()))
				self.cvcard=str(self.cvv.get())
				self.Mes=str(self.Mescard.get())
				self.año=str(gencc.ran(23,30))
				if len(self.cvcard)<3 and len(self.Mes)<2:
					self.cvcard="0"+self.cvcard
					self.Mes="0"+self.Mes
			
			elif self.Bincard.get() and not self.Mescard.get() and not self.acard.get() and not self.cvv.get():
				self.Credit=gencc.generador(str(self.Bincard.get()))
				self.Mes=str(gencc.ran(1,12))
				self.año=str(gencc.ran(23,30))
				self.cvcard=str(gencc.ran(10,99))
				if len(self.Mes)<2  and len(self.cvcard)<3:
					self.Mes="0"+self.Mes
					self.cvcard="0"+self.cvcard
			else:
				messagebox.showinfo("Ingresa tus datos","Hubo un error en los datos proporcionados")
				
			
#			self.Result.set(self.Credit+"|"+self.Mes+"|"+self.año+"|"+self.cvcard)
			self.Result.set(self.Credit+"|"+self.Mes+"|"+self.año+"|"+self.cvcard)
#			self.Credit.delate()
#			self.Mes.delate()
#			self.año.delate()
#			self.cvcard.delate()


#Menu opciones
		self.menu=Menu(self)
		self.barra=Menu(self.menu,tearoff=0)
		self.barra.add_command(label="open")





#----------------Frame						
		
		self.frame=Frame(self,relief="sunken")
		self.config(width=250,height=250,bg="black",relief="groove")
		
		#texto
		self.Bincard=StringVar()
		self.Credit=""
		self.Mescard=StringVar()
		self.Mes=""
		self.acard=StringVar()
		self.año=""
		self.cvv=StringVar()
		self.cvcard=""
		self.Result=StringVar()
		self.Rcard=""
		self.Result2=StringVar()
		
#Entradas		
		
		#Entrada del campo generador
		self.bin=Entry(self,textvariable=self.Bincard,relief="sunken",bg="black",fg="green2")
		self.bin.grid(row=0,column=0,pady=30)
		self.mes=Entry(self,textvariable=self.Mescard,bg="black",fg="green2")
		self.mes.grid(row=1,column=0,padx=20)
		self.año=Entry(self,textvariable=self.acard,bg="black",fg="green2")
		self.año.grid(row=2,column=0,pady=30)
		self.cvv=Entry(self,textvariable=self.cvv,bg="black",fg="green2")
		self.cvv.grid(row=3,column=0,pady=10)
		

		
		
		#Salida del chequeo
		self.resultado=Entry(self,textvariable=self.Result,width=25,bg="black",fg="green1")
		self.resultado.grid(row=6,column=0)
	#	self.resultado2=Entry(self,textvariable=self.Result2,width=25)
	#	self.resultado2.grid(row=7,column=0)

		
		
		#Mensaje chec
	#	self.pantalla=Entry(self,bg="gray30",width=20)
	#	self.pantalla.grid(column=a1,row=8)
		
		
		#Etiquetas de las entradas del generador
		self.etiqueta=Label(self,text="Numero de CC ")
		self.etiqueta.grid(row=0,column=1)
		self.etiqueta.config(bg="black",font=("Arial",8,"bold"),fg="DarkOrange2")
		self.etiqueta2=Label(self,text="Mes")
		self.etiqueta2.grid(row=1,column=1)
		self.etiqueta2.config(bg="Black",font=("Comic",8,"bold"),fg="orange3")
		self.etiqueta3=Label(self,text="Año")
		self.etiqueta3.grid(row=2,column=1)
		self.etiqueta3.config(bg="Black",font=("Arial",8,"bold"),fg="DarkOrange2")
		self.etiqueta4=Label(self,text="Cvc o Cvv ")
		self.etiqueta4.grid(row=3,column=1)
		self.etiqueta4.config(bg="Black",font=("Comic",8,"bold"),fg="DarkOrange2")
		self.etiqueta5=Label(self,text="Bin generado")
		self.etiqueta5.config(bg="Black",font=("Comic",8,"bold"),fg="PaleGreen2")
		self.etiqueta5.grid(row=6,column=1)
		
	#	self.text=Text(self,width=100,height=100)
	#	self.text.grid(row=4,column=2)
		
		
		#Botones 
		self.boton=Button(self,text="GenStone",command=Checker,font=("Comic",10,"bold"),relief="sunken")
		self.boton.grid(row=4,column=0,pady=30)
		self.boton.config(fg="Green3",bg="Gray15")
		
		
		
raiz=Raiz()


	
raiz.mainloop()
		