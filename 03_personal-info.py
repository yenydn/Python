#           03_personal-info.py
#
#          ***********************
#
#funcion que comprueba la cantidad de letras
def funcion():
    x=input()
    if len(x) <= 1:
      print('debe introducir más de 2 caracteres')
      funcion()
    else:
      datos[c]=x

#diccionario
datos={
  'nombre': '',
  'apellido':'',
  'telefono':'',
  'ciudad':'',
  'edad':''
  }

#bucle que aplica la funcion
for c in datos:
  print ('introduzca su ' + c + ': ')
	
  funcion()

#bucle que aplica el print
for i in datos:
  print ( 'su ', i , ' es : ' ,datos[i])
