'''
Coroutines: Coroutines in Python are a type of function that can pause execution and return control to the caller, while also retaining their own state. 
They allow for cooperative multitasking, meaning that multiple coroutines can run within a single thread, taking turns using the CPU.
Coroutines are defined using the async def syntax, and can be used with the await keyword to pause their execution and allow other coroutines to run. 
Coroutines can also send and receive data through the use of asyncio and yield.
Coroutines are commonly used for I/O-bound operations, such as reading from a file or making a network request, where the process may need to wait for data to become available. 
By using coroutines, the program can continue to make progress and work on other tasks while waiting for the I/O operation to complete.
'''

import time

def searcher():
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good."
    time.sleep(4)

    while True:
        text = (yield) # this implies thatt we are going to use searcher as coroutine
        if text in book:
            print("Your text is in the book")
        else:
            print("Your text is not in the book")
        

search = searcher()
next(search)
search.send("harry") # first time it will take time since it is reading the book which is taking 4 seconds
input("Press any key to continue")
search.send("harry and")  # this time it wont take much time since it will run from while True: