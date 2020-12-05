

def peaks(data):
    #new blank list
    output = []
    # iterating over the list indexes
    for i in range(1,len(data)-1):
    #extracting indices and comparing values
        if data[i] > data[i+1] and  data[i] > data[i-1]:
            output.append(i)
    return output

#       0  1  2  3  4  5  6  7  8  9 ...
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#peaks(data)        






def valleys(data):
    #new blank list
    output1 = []
    # iterating over the list indexes
    for i in range(1,len(data)-1):
    #extracting indices and comparing values to find index with higher left & right
        if data[i] < data[i+1] and  data[i] < data[i-1]:
            output1.append(i)
    return output1
#valleys(data)    



def peaks_and_valleys(p,v):
    #new list to add previous function data to
    p = peaks(data)
    v = valleys(data)
    #adding lists to the new function list
    p.extend(v)
    p.sort()
    print(p)

peaks_and_valleys(peaks,valleys)    