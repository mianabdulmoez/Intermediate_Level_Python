#Type is function which show the type of value which may (int)(str)(float)
# Type_casting is method in which the original type into other 

var1 ="Hello world"#Sting
var2 ="End this"
var3 = 24 #Integer
var4 = 21.8 #Float
var5 ="54" #string
var6 ="78"
# This is type checking method.by us print(type())
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))
# print(int(var1)) This cant be possible because var1 is srting which can't
# change in int or float
print(str(var4))
print(str(var5))
print(str(var6))
print(var5 + var6)#But we can use it like that
print(int(var5) + int(var6))#int can be add after converting from string
print(float(var4))
print(int(var4))#This convert it into int from float

# This is Type casting method in which change orignal type
print(10*"Hello world\n")
print(10*"var1\n")
print(10*str(int(var5) + int(var6)))
print(10*var3)#But
print(10*str(var3))