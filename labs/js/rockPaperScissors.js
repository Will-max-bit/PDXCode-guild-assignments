let rock_option = document.querySelector('#rock_option')
let paper_option = document.querySelector('#paper_option')
let scissors_option = document.querySelector('#scissors_option')
let btn_click = document.querySelector('#btn_click')
let solution = document.querySelector('#solution')


let options = ['rock', 'paper', 'scissors']
function rockPaperScissors() {
    while (true) {
        let rand_Choice = Math.floor(Math.random() * options.length)
        let compChoice = options[rand_Choice]
        let userChoice;
            if (paper_option.checked){
                userChoice = paper_option.value
            }
            else if (rock_option.checked){
                userChoice = rock_option.value
            }
            else if (scissors_option.checked) {
                userChoice = scissors_option.value
            }

        if (userChoice === compChoice) {
            return ("It's a tie")
        }
        else if (userChoice === 'rock' && compChoice === 'paper') {
            return("You have lost")
        }

        else if (userChoice === 'rock' && compChoice !== 'scissors') {
            return ("You have won")
        }

        else if (userChoice === 'paper' && compChoice !== 'scissors') {
            return ("You have lost")
        }

        else if (userChoice === 'paper' && compChoice !== 'rock') {
            return ("You have won")
        }

        else if (userChoice === 'scissors' && compChoice !== 'rock') {
            return ("You have lost")
        }

        else if (userChoice === 'scissors' && compChoice !== 'paper') {
            return ("You have won")
        }

    }
}



document.getElementById("btn_click").addEventListener('click', function () {
    let output = rockPaperScissors()
    solution.innerText = output
    

})