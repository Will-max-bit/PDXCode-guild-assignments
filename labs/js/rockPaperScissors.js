

let options = ['rock', 'paper', 'scissors']

while (true) {
    let rand_Choice = Math.floor(Math.random() * options.length)
    let compChoice = options[rand_Choice]
    let userChoice = prompt('Pick between rock paper or scissors').toLowerCase();

    if (userChoice === compChoice) {
        alert("It's a tie")
    }
        else if (userChoice === 'rock' && compChoice === 'paper'){
            alert("You have lost")
        }

        else if (userChoice === 'rock' && compChoice !== 'scissors'){
            alert("You have won")
        }

        else if (userChoice === 'paper' && compChoice !== 'scissors'){
            alert("You have lost")
        }

        else if (userChoice === 'paper' && compChoice !== 'rock'){
            alert("You have won")
        }

        else if (userChoice === 'scissors' && compChoice !== 'rock'){
            alert("You have lost")
        }

        else if (userChoice === 'scissors' && compChoice !== 'paper'){
            alert("You have won")
        }
        
}