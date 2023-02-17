'''
Function Caching: Function caching is a technique used to improve the performance of functions that are called repeatedly with the same arguments.
The idea is to store the results of previous function calls so that they can be quickly returned if the function is called again with the same arguments.
In Python, function caching can be implemented using a decorator. 
A decorator is a special type of function that can be used to modify the behavior of another function. Here's
'''

import time
from functools import lru_cache

@lru_cache(maxsize=3) # this is a decorator, maxsize tells how many values you want to store of this function. More the maxsize, more local memory will be used. It will only save last three recent values.
def some_work(n):
    # some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some code...")
    some_work(3) # first time this task will take 3 seconds
    print("done")
    some_work(3) # since value is already stored in the lru_cache memory, this time it wint take 3 seconds
    print("called again")