'''
Using else with for loops
'''

khana = ['roti', 'sabzi', 'chawal']

for item in khana:
    print(item)

else: # you can only use else with for loop when whole of the items are iterated completely. 
#Note if by any chance for loop got break then the else statement will not be executed.
    print('This for loop ended properly')