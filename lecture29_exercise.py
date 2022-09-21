'''
Pattern Printitng:
Take input from user of 1 or 0 where 1 means true and 0 means false
after take input from user of an integer
if pattern is true print in increasing order
if pattern is false print in decreasing order
'''


boolean_choice = int(input(
    "Enter your choice of number: \n1 for pattern printing in increasing order\n0 for pattern printing in reverse order\n"))
highest_size_pattern = int(input("enter maximum number of size"))

if boolean_choice == 1:
    string = ""
    star = 0
    while star < highest_size_pattern:
        string += "*"
        print(string+"\n")
        star += 1

elif boolean_choice == 0:
    string = "*"*highest_size_pattern
    star = 0
    while star < highest_size_pattern:
        print(string+"\n")
        string = string[:-1]
        star += 1

else:
    print("wrong choice")
