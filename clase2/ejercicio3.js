//Ejecutar con 'ejercicio3.html'
let fecha1= /* '12/12/1234'// */prompt('Ingresa una fecha en formato DD/MM/AAAA: ')
let fecha2= /* '12/12/1234'// */prompt('Ingresa una fecha en formato DD/MM/AAAA: ')

const day1 = fecha1[0]+fecha1[1]
const month1 = fecha1[3]+fecha1[4]
const year1 =fecha1[6]+fecha1[7]+fecha1[8]+fecha1[9]
console.log('day1: ',day1);
console.log('month1: ',month1);
console.log('year1: ',year1);

const day2 = fecha2[0]+fecha2[1]
const month2 = fecha2[3]+fecha2[4]
const year2 =fecha2[6]+fecha2[7]+fecha2[8]+fecha2[9]
console.log('day2: ',day2);
console.log('month2: ',month2);
console.log('year2: ',year2);

const date1=parseInt(year1+month1+day1)
const date2=parseInt(year2+month2+day2)

const subtract =date1-date2
console.log(subtract);
if (date1<subtract){
    console.log(fecha1,'es la fecha mas actual. Mientras que ',fecha2, 'es la fecha mas antigua');
}else{
    console.log(fecha2,'es la fecha mas actual. Mientras que ',fecha1, 'es la fecha mas antigua');
}