import requests
from datetime import datetime
import re
import pprint
import math
import statistics
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




# def variance(nums):
#     m = mean(nums)
#     total = 0
#     for num in nums:
#         total += (num - m)**2
#     return total / len(nums)



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

data = get_data()
nums = []
for datum in data:
    nums.append(datum[1])
print("variance of water is % s"%(statistics.variance(nums)))
date_and_water = sorted(data, key=getkey, reverse=True)
water_data = date_and_water[0]
dtg = date_and_water[0]
date_group = (dtg[0].strftime('%d-%b-%Y'))
print(f'on {date_group} there was {water_data[1]} inches of water')
#water = water_nums(data)
mean = calculate_mean(data)
print(f'The mean is {mean}')



        





