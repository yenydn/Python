#
#             5_calculator.py
#             ---------------
#

#Bucle que comprueba la introducción del número
while True:
	try:
		num1=float(input('ingrese un primer número: '))
		num2=float(input('ingrese un segundo número: '))
		break
	except ValueError:
		print('Por favor, introduzca un dato válido')

#Funcionalidades
print('Opciones','1 = Sumar','2 = Restar','3 = Multiplicar','4 = Dividir','5 = Exponenciar',end='\n',sep="\n")

#Sentencia que solicita la acción
seleccion=input('indique que accion desea realizar: ')

#Función que ejecuta la acción
def calculadora():
	if seleccion=="1":
	 print (num1 + num2)
	elif seleccion=="2":
 	 print (num1 - num2)
	elif seleccion=="3":
	 print (num1 * num2)
	elif seleccion=="4":
	  print (num1 / num2)
	elif seleccion=="5":
	  print (num1 ** num2)
	else:
	 print ('opcion incorrecta')

calculadora()
