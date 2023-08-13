# Python always start counting from 0
# main thing in slicing that it didn't  exe cute the last numer like[0:5]
# it print the word from 0-4 mean these are the 5 words 
# it exclude the last number 5 such as it print 0-4
# This line contain on 0_18 words
rozi="Rozi is a bad girl"
print(rozi)
print(rozi[0])
print(rozi[1])
print(rozi[2])
print(rozi[3])
# print(rozi[0:3]) here we see that the it print words from 0-2 mean these are the 3 words
print(rozi[0:4])
# so checking the length of line by using len()
print(len(rozi))
print(rozi[0:18])
# We can also print it like this
# print(rozi[50]) so here we the python did'nt recognize the 50th word which is not in line
# But it can print this from 0 any where
print(rozi[0:45])
print(rozi[:])
print(rozi[0:])
print(rozi[:18])
print(rozi[:5])
print(rozi[5:])
print(rozi[0:0])
