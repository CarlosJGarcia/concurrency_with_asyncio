# Generating and timing the Fibonacci sequence
# Multithreaded Python application
# While it's running, open $ htop 
# Instead of one core 100% busy, the OS scheduler will assign the two threads to two different cores
# The GIL serializes execution — only one thread runs Python bytecode at a time
# Result: no paralelism, no speedup, just GIL-switching overhead 

import time
import threading
 
# Calculates and prints a specific number in the Fibonacci sequence
# The classic way to generate heavy and sustained CPU load
# Uses nested functions and recursion
def print_fib(number):                         # Outer function: takes the input and prints the output
    def fib(n):                                # Nested function: can only be called from print_fib()
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)    # Recursion: the function definition calls himself
 
    print(f"Number {number} in the Fibonacci sequence is {fib(number)}")

     
def fibonacci_with_threads():
    # Initializes new thread objects, pointing to the function 
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))
 
    fortieth_thread.start()                   # Start running fortieth_thread
    forty_first_thread.start()                # Start running forty_first_thread
 
    fortieth_thread.join()                    # Wait until fortieth_thread has finished
    forty_first_thread.join()                 # Wait until forty_first_thread has finished
 
 
print("\nStarting 40 and 41")
start_time = time.time()
fibonacci_with_threads()
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time: {execution_time_seconds:.2f} seconds\n")