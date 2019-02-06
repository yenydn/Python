#         
#           02_list-dict.py
#
#	          **************		
#
#crear una lista que contenga varios strings, otra #con integers y otra con strings, integrers y floats

listString=["uno","dos","tres","manzana","pera"]

listInt=[1,7,10,22,42,100]

listVarios=[1.2,"manzana","jarron",100,4.7,5.2,2,1]

#crear la sentencia para imprimir esas listas por pantalla

print("Esta es la lista de los Strings: ","\n",  listString,"\n",  "Esta es la lista de los Integers: ","\n",  listInt,"\n", "Esta es la lista de Strings, Floats e Integers: ","\n",  listVarios,"\n")

#Crear 3 variables, cada una con el último valor de una de las listas

valorUno=listString[len(listString)-1]

valorDos=listInt[len(listInt)-1]

valorTres=listVarios[len(listVarios)-1]

#Crear una sentencia para imprimir, por pantalla, un texto, y concatenar la información de las variables.

print("Valor Uno:" , valorUno, "Valor dos:", valorDos, "Valor tres:", valorTres, sep="\n")

#Crear un diccionario de vuestras películas/obras favoritas (clave: autor,valor:película)

Obras={
  "Lewis Carroll":"Alice in wonderland",
  "J.R.R. Tolkien":"El Silmarillion",
  "Antoine de Saint-Exupéry": "El Principito",
  "Assimov": "Cuevas de Acero"
}

#Crear sentencia para imprimir por pantalla todo el diccionario.
print("\n","Diccionario con Obras:")
for i in Obras:
  print (i, ":" , Obras[i])

#Crear sentencia para imprimir por pantalla sólo las claves del diccionario

print ("\n","Claves del diccionario: ",Obras.keys(),sep="\n")

#Crear sentencia para imprimir por pantalla sólo los valores del diccionario.

print ("\n","Claves del diccionario: ",Obras.values(),sep="\n")
