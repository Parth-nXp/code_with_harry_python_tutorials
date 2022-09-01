var1 = "hello World"  # string
var2 = 20  # int
var3 = 20.5  # float
print(type(var3))

'''
Typecasting
'''
# int to float
print(float(var2))
# float to int
print(int(var3))
# int to string
print(str(var2))

'''
String Muliplication
'''

print((var1 + '\n') * 5)

'''

User Input

'''

print("Enter your number: ")
inpnum = input()
print("Your number is: ", int(inpnum)+10)
