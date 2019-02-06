#
#             06_for.py
#             ---------------
#
personas=('María','Marta','Miguel','Manuel','Mary','Moises')
selected=[];

for i in personas:
  for x in i:
    if x=="a" or x=="A":
      selected.append(i)

#se agrega un conjunto para evitar repeticiones dentro de la lista
selected=set(selected)

print ('Lista con todos los nombres: ', personas)
print ('Lista selected: ',selected,end='\n')
