'''
Try Except Exception Handling: Used to smoothly run the code. Most of the times when the program is running if error occurs whole program stops to execute.
To overcome this problem Try excep exception handling is used in which you can try to run a part of program and if it throws an error you can handle that error and also execute other part of code.
This is generally used when you want to access internet from your program, suppose in some case internet is not working than in that case your code will not run. In that case this can be usefull
'''

a = input("Enter the first number")
b = input("Enter the second number")


try:  # The try block lets you test a block of code for errors.
    print("Sum of the two numbers is ", int(a)+int(b))

except Exception as error:  # The except block lets you handle the error.
    print(error)

print("Your program will run smoothly after")
