'''
Else & Finally in try except:
'''


# this is how you run the try-except block

try:
    open("something.txt")

except Exception as e:
    print(e)


print("Important work done")

# try-else-finally vlock

f1= open("Harry.txt")

try:
    f = open("somethin.txt")

except Exception as e:
    print(e)

else:
    print("This will only run if except is not running.")

finally: # this is used for code cleanup. if we have openeed so many files we can close using this
    print("This will always run no matter code goes into try or exception")
    f1.close()    

print("Importnat work done")