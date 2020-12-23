import requests
from datetime import datetime
import re
import pprint
import math
# response = requests.get('https://or.water.usgs.gov/non-usgs/bes/shipyard.rain')
# print(response.text)




def get_data():
    with open('Shipyard_Rain_Gage.rain', 'r') as file:
        text = file.read()
    dates = re.findall(r'(\d\d-\w\w\w-\d\d\d\d)\s+(\d+)',text)
    data = []
    for datum in dates:
        date = datetime.strptime(datum[0], '%d-%b-%Y')
        daily_total = int(datum[1]) * 0.01
        data.append((date, daily_total))
    return data


def calculate_mean(data):
    mean_tally = 0
    for dat in data:
        mean_tally += dat[1]
    mean_total = mean_tally / len(data)
    return mean_total 

def water_nums(nums):
    output = []
    for num in nums:
        output.append(num[1])
    return output

def variance(nums):
    m = mean(nums)
    total = 0
    for num in nums:
        total += (num - m)**2
    return total / len(nums)


# >>> def getKey(item):
# ...     return item[0]
# >>> l = [[2, 3], [6, 7], [3, 34], [24, 64], [1, 43]]
# >>> sorted(l, key=getKey)
# [[1, 43], [2, 3], [3, 34], [6, 7], [24, 64]]

def getkey(item):
    return item[1]


def most_rain(items):
    output = []
    for item in items:
        if item[1] > 0.1:
            output.append(item)
        for i in range(len(output)):
            pass
    #return output 

#if i >= len(alpha):

data = get_data()
test = sorted(data, key=getkey, reverse=True)
print(test[0])
water = water_nums(data)
mean = calculate_mean(data)
print(f'The mean is {mean}')
#print(variance(water))


        





