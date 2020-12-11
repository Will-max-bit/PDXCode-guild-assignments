import math
#Dictionary will be used to convert integer to string
nums = {
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
    100: 'one hundred and',
    200: 'two hundred and',
    300: 'three hundred and',
    400: 'four hundred and',
    500: 'five hundred and',
    600: 'six hundred and',
    700: 'seven hundred and',
    800: 'eight hundred and',
    900: 'nine hundred and',

}


def changling_nums(number):
    #One_digit variable converts whole (def 'number')integer (109 etc) into single digit (>>>9)
    one_digit = number % 10
    #hundreds variable converts whole (def 'number')integer (109 etc) into 100's digit (>>>100)
    hundreds = ((number // 100)*100)
    #teens variable converts whole (def 'number')integer (109 etc) into 10's digit (>>>10) 
    teens = (((number % 100)//10)*10)
    # if number argument after conversion can be found in dict the if statement will run and program will exit, 19,8 10, etc
    if number in nums:
        print(nums[number])
    # if number argument after conversion is in hundreds but with no 10's place the if statement below will run, 109,206, 303 etc
    elif hundreds in nums and teens not in nums and one_digit in nums:
        print(nums[hundreds] + '-' + nums[one_digit])
    # if number argument after conversion is not in hundreds but with 10's place if statement below will run, 89,16, 98 etc
    elif hundreds not in nums and teens in nums and one_digit in nums:
        print(nums[teens] + '-' + nums[one_digit])
    # if number argument after conversion is  in hundreds and with 10's place if statement below will run, 189,316, 998 etc
    elif hundreds in nums and teens in nums and one_digit in nums:
        print(nums[hundreds] +' '+ nums[teens] + '-' + nums[one_digit])
    
    



changling_nums(969)

