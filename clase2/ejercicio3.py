fecha1=input('Ingresa una fecha en formato DD/MM/AAAA: ')
fecha2=input('Ingresa una fecha en formato DD/MM/AAAA: ')

# 12/12/1234
# 0123456789
day1=fecha1[0:2]
month1=fecha1[3:5]
year1=fecha1[6:10]
print('day1: ',day1)
print('month1: ',month1)
print('year1: ',year1)

day2=fecha2[0:2]
month2=fecha2[3:5]
year2=fecha2[6:10]
print('day2: ',day2)
print('month2: ',month2)
print('year2: ',year2)

date1= int(year1+month1+day1)
date2= int(year2+month2+day2)

subtract = int(date1)-int(date2)

if date1 < subtract:
    print(str(fecha1),'es la fecha mas actual. Mientras que ',str(fecha2), 'es la fecha mas antigua.')
if date1 > subtract:
    print(str(fecha2),'es la fecha mas actual. Mientras que ',str(fecha1), 'es la fecha mas antigua.')
