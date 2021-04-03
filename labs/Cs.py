
# import math
# #linear search
# def linear_search(nums, value):
#     numbers = nums
#     output = []
#     for i,number in enumerate(numbers):
#         if number == value:
#             output.append(number)
#     return output


# print('-----------------------')

# def linear_search1(nums, value):
#     for i in range(len(nums)):
#         if nums[i] == value:
#             return i

# # print(linear_search1(nums, 3))
# nums = [1,2,3,4,5,6,7,8]
# len_nums = len(nums)
# t = 3
# #binary search
# def bine_search(nums, len_nums, t):
#     sort_nums = sorted(nums)
#     low = sort_nums[0]
#     high = sort_nums[-1]
#     # mid = len_nums / 2
#     while low < high:
#         mid = math.floor((low + high)/ 2)
#         if nums[mid] < t:
#             low = (mid - 1)
#         elif nums[mid] > t:
#             high = (mid-1)
#         else:
#             return mid
            
#     return 'unsuccessful'

# print(bine_search(nums,len_nums, t))

# # bubble sort

# def bubble_sort(nums):
#     num_len = len(nums)


class Node:
    def __init__(self, item , next=None):
        self.item = item
        self.next = next
    
    def __str__(self):
        return f'({self.item}, {self.next}'
class Stack:
    def __str__(self):
        self.root = None

    def push(self, element):
        if self.root is None:
            self.root = Node(elemet, None)
        else:
            node = Node(element, self.root)
            self.root = node
    
    
    def pop(self, item):
        if self.root == None:
            return None
        else:
            pop1 = self.root
            self.root = self.root.next
            # pop1.next = None
            return pop1.item


    


    def __str__(self):
        output= ''
        n = self.root
        while n is not None:
            output += f'({n.time}, {n.next is not none})'
            n = n.next
        return output

s = Stack()
s.push('apple')
s.push('bananas')
s.push('pears')
print(s)