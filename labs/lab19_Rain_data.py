import requests
from datetime import datetime
import re
import pprint
import math
import statistics

#Function opens data file and parses the data for date and first value
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

#function creates a 0 variable that will be used to total the rain amount data
def calculate_mean(data):
    mean_tally = 0
    for dat in data:
        mean_tally += dat[1]
    mean_total = mean_tally / len(data)
    return mean_total 


#item[1] is the rain amount value index of data, value of item[1] will be used to sort
def getkey(item):
    return item[1]

#using variance from the statistics module to get the variance
data = get_data()
def variance():
    nums = []
    for datum in data:
        nums.append(datum[1])
    return ("The variance of water is % s"%(statistics.variance(nums)))

#sorted the list of tuples (data) and reversing to make the highest number first
date_and_water = sorted(data, key=getkey, reverse=True)

def water_most(x):
    water_data = x[0]
    dtg = water_data[0]
    dtg = date_and_water[0]
    date_group = (dtg[0].strftime('%d-%b-%Y'))
    return (f'on {date_group} there was {water_data[1]} inches of water')


print(f'The mean is {calculate_mean(data)}inches')
print(variance())
print(water_most(date_and_water))






        





