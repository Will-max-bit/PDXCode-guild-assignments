
#-------------------------lab attempts-------its good----------------------------#
#conversions = {1: 1 * 0.3048, 2: 2 * 0.3048, 3: 3 * 0.3048 }
#user_number = input('What number would you like to convert to meters?: ')
#user_convert_number = float(user_number)
#print(f'The distance of {user_convert_number} feet in meters is: {conversions[user_convert_number]}')

#------------------lab attempt2-----------------------------------------------------#
user_unit_choice = input('What unit would you like to meters? \n mi, ft, inch or yd:  ')
user_choice_number = input('What number would you like to use? ')
usable_usernumber = int(user_choice_number)
convertables = {'mi':usable_usernumber * 1609.34, 'ft': usable_usernumber * 0.3048,'inch': usable_usernumber * 39.3701, 'yd': usable_usernumber * 1.09361 }
print(f'The distance of {usable_usernumber} in {user_unit_choice} is {convertables[user_unit_choice]} in meters')




