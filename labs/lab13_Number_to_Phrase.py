import math
#Dictionary will be used to convert integer to string
nums = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'one hundred',
    200: 'two hundred',
    300: 'three hundred',
    400: 'four hundred',
    500: 'five hundred',
    600: 'six hundred',
    700: 'seven hundred',
    800: 'eight hundred',
    900: 'nine hundred',

}
# nums2 = {
#     100: 'one hundred',
#     200: 'two hundred',
#     300: 'three hundred',
#     400: 'four hundred',
#     500: 'five hundred',
#     600: 'six hundred',
#     700: 'seven hundred',
#     800: 'eight hundred',
#     900: 'nine hundred',
# }


def changling_nums(number):
    #One_digit variable converts whole (def 'number')integer (109 etc) into single digit (>>>9)
    one_digit = number % 10
    #hundreds variable converts whole (def 'number')integer (109 etc) into 100's digit (>>>100)
    hundreds = ((number // 100)*100)
    #teens variable converts whole (def 'number')integer (109 etc) into 10's digit (>>>10) 
    teens = (((number % 100)//10)*10)
    # if number argument after conversion can be found in dict the if statement will run and program will exit, 19,8 10, etc
    if number in nums:
        return nums[number]
    # if number argument after conversion is in hundreds but with no 10's place the if statement below will run, 109,206, 303 etc
    elif hundreds in nums and teens not in nums and one_digit in nums:
        return nums[hundreds] + '-' + nums[one_digit]
    # if number argument after conversion is not in hundreds but with 10's place if statement below will run, 89,16, 98 etc
    elif hundreds not in nums and teens in nums and one_digit in nums:
        return nums[teens] + '-' + nums[one_digit]
    # if number argument after conversion is  in hundreds and with 10's place if statement below will run, 189,316, 998 etc
    elif hundreds in nums and teens in nums and one_digit in nums:
        return nums[hundreds] +' '+ nums[teens] +  nums[one_digit]
    return
    
# for i in range(1,1000):
#     print(i, changling_nums(i))    


quest = int(input('Pick a number: '))
print(changling_nums(quest))

