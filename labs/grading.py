def grades(number):
    if number >= 90:
        if number % 10 > 5: 
            print('you got an A+')
        elif number % 10 < 5:
            print('you got an A-')
    elif number >= 80:
        if number % 10 > 5: 
            print('you got an B+')
        elif number % 10 < 5:
            print('you got an B-')
    elif number >= 70:
        if number % 10 > 5: 
            print('you got an C+')
        elif number % 10 < 5:
            print('you got an C-')
    elif number >= 60:
        if number % 10 > 5: 
            print('you got an D+')
        elif number % 10 < 5:
            print('you got an D-')
    elif number <= 59:
        print('you got an F')

while True:
    grad_quest = input('Would you like to convert your grade? \n yes or no: ')
    if grad_quest == 'no':
        print('Have a good day')
        break
    use_grade = int(input('please enter a number grade: '))
    grades(use_grade)







    
