name1= input('Nombre de la persona 1: ')

name2 = input('Nombre de la persona 2: ')

names = (name1, name2)

order=sorted(names)



if name1==name2:
    print ('Los nombres son iguales')
else:
    print('Los nombres son diferentes')

if order==name1 and name2:
    print(order)
    print (name2, ' va primero alfabeticamnete que ', name1)
else :
    print(order)
    print (name1, ' va segundo alfabeticamnete que ', name2)

