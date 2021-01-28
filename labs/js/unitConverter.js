dictConversions = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'yd': 09.144,
    'in': 0.0254,
    'mt': 1,
}

let first_unit = document.querySelector('#first_unit')
let second_unit = document.querySelector('#second_unit')
let number_length = document.querySelector('#number_length')
let solution = document.querySelector('#solution')
let ddl = document.querySelector('#ddl')
let ddl2 = document.querySelector('#ddl2')

solution.style.color = 'lightgrey'

document.getElementById('btn_click').addEventListener('click', function () {
    let output = (dictConversions[first_unit.value] * number_length.value) / dictConversions[second_unit.value]
    console.log(output)
    solution.innerText = output
    solution.style.color = 'black'
})