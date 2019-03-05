def Suma():
    print( 'resultado: ',round( a+ b,2))
def Resta():
    print( 'resultado: ',round(a- b,2))
def Multiplicacion():
    print( 'resultado: ', round( a* b,2))
def Division():
    print( 'resultado: ',round( a/ b,2))
def Exponenciacion():
    print( 'resultado: ', round( a** b,2))

def comprobacion():
    try:
        global a,b
        a=float(input('Introduzca un primer valor: '))
        b=float(input('Introduzca un segundo valor: '))
        opcion[accion]()
    except:
        print('Ha indicado una acción incorrecta')

print(
'  MENÚ'.center(20),
'________'.center(20),
'1=Suma','2=Resta','3=Multiplicacion','4=Division','5=Exponenciacion','6=Salir',sep='\n',end='\n'
)
opcion={1:Suma,2:Resta,3:Multiplicacion,4:Division,5:Exponenciacion,6:'Salir'}

while True:
    try:
        accion=int(input('\n'' Indique con un número que desea hacer: '))
        if accion==6:
            print('usted ha decidido', opcion[accion])
            break
        elif accion not in opcion.keys():
            print('esa opcion no está incluida')
        else:
          comprobacion()
    except: 
        print('Ha indicado una acción incorrecta')
