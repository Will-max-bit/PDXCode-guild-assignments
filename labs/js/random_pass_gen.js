


const letters_Numbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
let pass = []
let i = 0
let useChoice = prompt('Pick a number')
while (i < useChoice) {
    let rand_Index = Math.floor(Math.random() * letters_Numbers.length)
    let randChar = letters_Numbers[rand_Index]
    pass.push(randChar)
    i += 1

    
}
alert(pass.join(''))