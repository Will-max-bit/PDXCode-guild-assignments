#types_of_people = 10
#x = f"There are {types_of_people} types of people"
#binary = "binary"
#do_not = "don't"
#y = f"Those who know {binary} and those who {do_not}."
#print(x)
#print(y)

#print(f"I said: {x}")
#print(f"I also said: {y}.")

#hilarious = False
#joke_evaluation = "Isn't that joke so funny?! {}"

#print(joke_evaluation.format(hilarious))

#w = "This is the left side of..."
#e = "a string with a right side."

#print(w + e)
#END

#print("Mary had a little lamb.")
#print("Its fleece was white as .".format('snow'))
#print("And everywhere that Mary went.")
#print("." * 10)

#end1 = 'c'
#end2 = 'h'
#end3 = 'e'
#end4 = 'e'
#end5 = 's'
#end6 = 'e'
#end7 = 'B'
#end8 = 'u'
#end9 = 'r'
#end10 = 'g'
#end11 = 'e'
#end12 = 'r'

#print(end1 + end2 + end3 + end4 + end5 + end6)
#print(end7 + end8 + end9 + end10 + end11 + end12)
#END

#formatter = "{} {} {} {}"
#
#print(formatter.format(1, 2, 3, 4))
#print(formatter.format("one", "two", "three", "four" ))
#print(formatter.format(True, False, False, True))
#print(formatter.format(formatter, formatter, formatter, formatter))
#print(formatter.format(
#    "Try your",
#    "Own text here",
#    "Maybe a poem",
#    "or a song about fear"
#    ))
#
#def hint_username(username):
#    if len(username) < 3:
#        print("Invalid username. Must be at least 3 characters long")

#def number_group(number):
#  if (number) > 0:
#    return "Positive"
#  if (number) < 0:
#    return "Negative"
#
#  return "zero"
#
#
#print(number_group(10)) #Should be Positive
#print(number_group(-5)) #Should be Negative
#print(number_group(0)) #Should be Zero

#def color_translator(color):
#	if color == "red":
#		hex_color = "#ff0000"
#	elif color == "green":
#		hex_color = "#00ff00"
#	elif color == "blue":
#		hex_color = "#0000ff"
#	"unknown":
#		hex_color = "unknown"
#	return "unknown"
#
#print(color_translator("blue")) # Should be #0000ff
#print(color_translator("yellow")) # Should be unknown
#print(color_translator("red")) # Should be #ff0000
#print(color_translator("black")) # Should be unknown
#print(color_translator("green")) # Should be #00ff00
#print(color_translator("")) # Should be unknown
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
  
# Driver code     
str1 = "Geeks for Geeks"
print(Convert(str1)) 