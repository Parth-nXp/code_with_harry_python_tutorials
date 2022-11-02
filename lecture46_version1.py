'''
if __name__=__main__ usage and necessity : Before executing code, Python interpreter reads source file and define few special variables/global variables. 
If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. 
If this file is being imported from another module, __name__ will be set to the module's name. 
Module's name is available as value to __name__ global variable. 
'''

def printhar(string):
    return f"Ye string harry ko dede {string}"

def addnum(num1,num2):
    return num1 + num2 + 5

print('and the name is ', __name__) # here the output will be __main__ but if we call this program in some other program than the output in that program will be the file name of that program 

if __name__== '__main__':
    print(printhar('thakur'))
    o = addnum(4,6)
    print(o)