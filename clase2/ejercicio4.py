orden =input('Indica con un numero la cantidad de pasos y con una letra mayúscula la dirección (ej. 5D, cinco pasos hacia la derecha): ')
pasos=orden[0:1]
dirección=orden[1:2]

# print(pasos)
flecha = ''
pasosFlecha = '-'*int(pasos)

if dirección == 'D':
    flecha = '=>'
    print(pasosFlecha + flecha)
if dirección == 'I':
    flecha = '<='
    print(flecha+pasosFlecha)

