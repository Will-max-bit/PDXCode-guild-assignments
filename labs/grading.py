def grades(number):
    if number >= 90:
        print('you got an A')
    elif number >= 80:
        print('you got an B')
    elif number >= 70:
        print('you got an C')
    elif number >= 60:
        print('you got an D')
    elif number <= 59:
        print('you got an F')

while True:
    grad_quest = input('Would you like to convert your grade? \n yes or no: ')
    if grad_quest == 'no':
        print('Have a good day')
        break
    use_grade = int(input('please enter a number grade: '))
    grades(use_grade)






    
