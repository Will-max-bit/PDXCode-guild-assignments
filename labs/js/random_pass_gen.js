let number_pass = document.querySelector('#number_pass')
let btn_click = document.querySelector('#btn_click')
let result_pass = document.querySelector('#result_pass')






function pass_gen() {
    const letters_Numbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    let pass = []
    let i = 0
    let useChoice = number_pass.value

    while (i < useChoice) {
        let rand_Index = Math.floor(Math.random() * letters_Numbers.length)
        let randChar = letters_Numbers[rand_Index]
        pass.push(randChar)
        i += 1
        
        


    }
    let something = pass.join('')
    return something
}



document.getElementById("btn_click").addEventListener('click', function () {
    let output = pass_gen()
    result_pass.value = output
    console.log(output)
    

})