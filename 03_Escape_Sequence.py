"""
An Escape Sequence character in Python is a sequence of characters that represents a single character.
It doesn't represent itself when used inside string literal or character.
"""

"""
Sequence is a function in python which perform by using 
'\' backward slash
"""
#Some types which use as escape sequence in python
#end is a new line character to connect two lines in code

#These are the two lines of code which are spearte.
print("Hello world")
print("This is mine world")
#No I can connect them them by using a sequence function which is:
#[end("") in these quotation marks we can use space , . etc which is needed]
print("Hello world", end=(" "))# I am using their space to make a sequence
print("This is mine world")

print("who is i am", end=(","))#so here i use comma to seprate line
print("I am Abdul Moeez")


# \ backward slash is escape sequence character.
# \n is a new line escape sequence character
print("c:\node")
print(10*"New World\n")#This print in 10 lines
#But to solve this problem we \\ like that
print("c:\\node")

# print("c:"computer") We cant write like this to get quote before computer
print("c:\"computer")#To print quote we use \ this
print("Hello\' Harry")#I cant use quote mark in doble qutation mark
print("How are you\' Ali")
print("How are you\, Ali")#It not use in under signs


#\t is use to get a tab space in code like that
print("He is a good boy He is also very sharp minded")
print("He is a good boy\n He is also very \t sharp minded")
#Here \n is spearte a new line and \t is space in very & sharp
print("He is a good boy He is also very sharp minded \t1")
