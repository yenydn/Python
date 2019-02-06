#
#             04_if.py
#           -------------
#

num=int(input('introduzca un numero: '))

if num < 20:
  print('el número es menor de 20: ', num)
elif num >= 20 and num <40:
  print('el número está entre 20 y 39: ', num)
elif num > 39 and num <60:
  print('el número está entre 40 y 59: ', num)
else:
  print('el numero esta entre 60 y más: ', num)
