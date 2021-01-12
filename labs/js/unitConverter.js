dictConversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'yd': 09.144,
    'in': 0.0254,
    'mt': 1,
}

let unit1 = prompt('First unit of measurement i.e ft-mi-km-yd-in-mt')
let unit2 = prompt('Second unit of measurement i.e ft-mi-km-yd-in-mt')
let numberChoice = prompt('pick a number')

let solution = (dictConversions[unit1] * numberChoice) / dictConversions[unit2]
alert(solution)



