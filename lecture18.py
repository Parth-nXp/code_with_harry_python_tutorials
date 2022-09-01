'''
Break and continue statements
'''

'''
Break statement
'''

i = 0  # initialize counter

while True:  # while loop condition which is always true
    print(i+1, end=" ")  # print the value of i
    if (i == 44):  # condition where i is 44
        break  # break the loop and exit the while loop
    i += 1  # i += 1 is the same as i = i + 1

# break statement is used to break out of a loop. It is used to exit the loop. This is the same as the while loop condition is false. It can be used in a for loop as well.
# while (1) or while True are infinite loops. These loops never stops until some condition is match

'''
Continue statement
'''
i = 0

while(1):  # while loop condition which is always true
    if (i < 5):  # condition where i is less than 5
        i = i+1  # increment
        continue  # continue statement return back to the while loop back and nothing after this gets executed
    print(i+1, end=" ")  # print the value of i

    if (i == 44):  # condition where i is 44
        break  # break the loop and exit the while loop

    i = i+1  # increment

# continue statement is used to return back to the initial point of the while loop. This is the same as the while loop started again. It can be used in a for loop as well.


'''
    Quiz
'''

while(1):
    number = input("Enter a number greater than 100: \n")
    if number.isnumeric():
        if (int(number) <= 100):
            print("Try again! \n")
            continue
        else:
            print("Congratulations your number is greater than 100 \n")
            break
    else:
        print("Try again! \n")
        continue
