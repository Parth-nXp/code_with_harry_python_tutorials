'''
Time module 
'''

from email.utils import localtime
from threading import local
import time


# program to find which runs faster while or for loop. For this we can use time module
initial = time.time() #time.time() returns the ticks in the python
# ticks- the floating-point numbers in units of seconds for time interval are indicated by tick in pythjon.
# Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch)
print(initial)
for i in range(45):
    print("This is harry bhai")
print(f'time to run for loop is {time.time()-initial} seconds')

initial2 = time.time()
k = 0
while (k<=45):
    print("This is harry bhai")
    k+=1
print(f'time to run for loop is {time.time()-initial2} seconds')

# to return the current local time
local_time = time.asctime(time.localtime(time.time()))
# time.time() returns the ticks starting from January1, 1970 12:00 am
# time.localtime() returns the ticks into tuple of local time but this is not in presentable manner
# time.asctime() converts the time into a presentable manner
print(local_time)

# Sleeptime- to create a delay in the program in seconds

k = 0

while (k<=45):
    print("This is harry bhai")
    k+=1
    time.sleep(2) # create a delay of 2 seconds