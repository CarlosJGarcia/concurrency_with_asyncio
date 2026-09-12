# Generating and timing the Fibonacci sequence
# Multithreaded Python application
# While it's running open $ htop to see how one core will be 100% busy
# Also the Ubuntu scheduled can assign each thread to a core, but the GIL will make that only one is active at a time (50% / 50%)

import time
import threading
 
# Calculates and prints a specific number in the Fibonacci sequence
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
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))
 
    fortieth_thread.start()
    forty_first_thread.start()
 
    fortieth_thread.join()
    forty_first_thread.join()
 
 
print("\nStarting 40 and 41")
start_time = time.time()
fibonacci_with_threads()
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time: {execution_time_seconds:.2f} seconds\n")