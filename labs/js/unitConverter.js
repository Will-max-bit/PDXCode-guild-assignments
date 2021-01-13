dictConversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'yd': 09.144,
    'in': 0.0254,
    'mt': 1,
}

// let unit1 = prompt('First unit of measurement i.e ft-mi-km-yd-in-mt')
// let unit2 = prompt('Second unit of measurement i.e ft-mi-km-yd-in-mt')
// let numberChoice = prompt('pick a number')

// let solution = (dictConversions[unit1] * numberChoice) / dictConversions[unit2]
// alert(solution)

let first_unit = document.querySelector('#first_unit')
let second_unit = document.querySelector('#second_unit')
let number_length = document.querySelector('#number_length')
let solution = document.querySelector('#solution')

solution.style.color = 'lightgrey'

document.getElementById('btn_click').addEventListener('click', function () {
    console.log(first_unit.value)
    console.log(second_unit.value)
    console.log(number_length.value)
    let output = (dictConversions[first_unit.value] * number_length.value) / dictConversions[second_unit.value]
    console.log(output)
    solution.innerText = output
})