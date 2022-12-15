a=1
suma=0
print(a)
while a<10:
    a = a + 1
    print(a)
    if a/2 == int(a/2):
        print('Es divisible por 2: '+ str(a))
        suma= suma+a
print('Suma es: '+ str(suma))