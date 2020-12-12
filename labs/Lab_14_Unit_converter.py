
#dictionary contains unit values of one converted into meters
mydict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'yd': 09.144,
    'in': 0.0254,
    'mt': 1,
}
#v1
'''
def metes(number):
    #function receives user input integer and multiplies by 1foot in meters
    result = number * 0.03048
    return result
#ask the user for number of feet
usequest = int(input('Enter a number of feet: '))
#returns function result of user integer of feet into meters
print(metes(usequest))
'''
#V2,3
# def metes(unit,number):
#     #we'll compare the user input (unit) to if statements until match
#     if unit == 'feet':
#         #user response is found in dictionary and multiplied by user input integer
#         result = mydict['ft'] * number
#         return result
#     if unit == 'miles':
#         result = mydict['mi'] * number
#         return result
#     if unit == 'kilometers':
#         result = mydict['km'] * number
#         return result
#     if unit == 'meters':
#         result = unit * 1
#         return result
#     if unit == 'yards':
#         result = mydict['yd'] * number
#         return result
#     if unit == 'inches':
#         result = mydict['in'] * number
#         return result
##Asking the user for a unit of measurement to be converted
# usequest1 = input('Enter unit of measurement \n feet, miles, meters, kilometers, yards or inches: ').lower()
#Asking user for integer value for the unit of measurement previously asked.
# usenumb = int(input('Enter a number to accompany the unit of measurement'))
# print(metes(usequest1,usenumb))

#V4
#Function to use user input as a number from the dictionary and used in the function below
def to_meters(text):
    #program searches dictionary for match to user input
    if text in mydict:
        return mydict[text]



#Function will take three parameters in order to convert between units
def master_func(unit1,unit2,number):
    #program will look for a match between the two user input measurements
    if unit1 == 'ft' and unit2 == 'mi':
        #program will convert first measurement(unit1) into meters then convert meters into the desired unit of length(unit2)
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'mi' and unit2 == 'ft':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'km' and unit2 == 'mt':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'mt' and unit2 == 'km':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'mt' and unit2 == 'mi':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'mi' and unit2 == 'mt':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'ft' and unit2 == 'mt':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    if unit1 == 'mt' and unit2 == 'ft':
        result = (to_meters(unit1) * number ) / mydict[unit2]
        return result
    
#asking user for the first unit of measurment
first_unit = input('What is the first unit of measurment \n ft, mi, mt, km,: ')
#asking user for second unit of measurment that will be in the final result
second_unit = input('What is the second unit of measurment to convert the first into \n ft, mi, mt, km: ')
#asking user for integer length of the first unit of measurement
nums = int(input('What is the number you\'d like to convert: '))
#returning the result to the user.
print(f'You converted {nums} {first_unit} into {master_func(first_unit,second_unit,nums) } {second_unit}')
    





