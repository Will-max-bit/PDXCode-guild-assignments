# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# Example
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")

#def print_days_in_month(month, days):
#    print( month + " has " + str(days) + " days.")
#
#
##def print_days_in_month_f(month, days):
##    print(f'{month} has {days} days.')
#    
#print_days_in_month("June", 30)
#print_days_in_month("July", 31)
#print_days_in_month("Beans are cool, can", 420)

#break
# def months_days(days):
#     june = 30 + days
#     july = 31 + days
#     print("June has " + str(june) "days")
#     print("July has " + str(july) "days")
# months_days("june ")
# months_days("july ")


# hi
# oh hi

#oh hello there


# eval(f"{dir('b')[-6][-1]}{dir('u')[65][0]}{dir('t')[40][1]}{dir('t')[44][-3]}{dir('s')[16][3]}(\"{msg_here}\")")

#msg_here = "it's a tuesday"
#thing = "stuff"
# p r i n t
#eval("print('fuck you')")
#eval(f"{dir('b')[-6][-1]}{dir('u')[65][0]}{dir('t')[40][1]}{dir('t')[44][-3]}{dir('s')[16][3]}(\"{msg_here}\")")

#def i(x):
    #eval(x)

#print(f"{dir('afdsa-asdfdsa-435hasd-as8d7cx-asdkjvyx')[(11-1)][3]}{dir([])[-3][4]}{dir([])[0][2]}{dir([])[1][3]}")


# a_list = ["stuff","thing","three", 4, thing]

# a_list[-1]

# 0 __add__
# 1 __class__
# 2 __contains__
# 3 __delattr__
# 4 __dir__
# 5 __doc__
# 6 __eq__
# 7 __format__
# 8 __ge__
# 9 __getattribute__
# 10 __getitem__
# 11 __getnewargs__
# 12 __gt__
# 13 __hash__
# 14 __init__
# 15 __init_subclass__
# 16 __iter__
# 17 __le__
# 18 __len__
# 19 __lt__
# 20 __mod__
# 21 __mul__
# 22 __ne__
# 23 __new__
# 24 __reduce__
# 25 __reduce_ex__
# 26 __repr__
# 27 __rmod__
# 28 __rmul__
# 29 __setattr__
# 30 __sizeof__
# 31 __str__
# 32 __subclasshook__
# 33 capitalize
# 34 casefold
# 35 center
# 36 count
# 37 encode
# 38 endswith
# 39 expandtabs
# 40 find
# 41 format
# 42 format_map
# 43 index
# 44 isalnum
# 45 isalpha
# 46 isascii
# 47 isdecimal
# 48 isdigit
# 49 isidentifier
# 50 islower
# 51 isnumeric
# 52 isprintable
# 53 isspace
# 54 istitle
# 55 isupper
# 56 join
# 57 ljust
# 58 lower
# 59 lstrip
# 60 maketrans
# 61 partition
# 62 replace
# 63 rfind
# 64 rindex
# 65 rjust
# 68 rstrip
# 69 split
# 70 splitlines
# 71 startswith
# 72 strip
# 73 swapcase
# 74 title
# 76 upper
# 77 zfill
# 78 beans
##print(11 % 5)
#def sum(x, y):
#		return(x+y)
#print(sum(sum(1,2), sum(3,4)))
#print((10 >= 5*2) and (10 <= 5*2))
#
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif word1 == word2:
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))