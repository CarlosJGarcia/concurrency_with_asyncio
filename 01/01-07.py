# Generating and timing the Fibonacci sequence
# Multiprocess Python application

# While it's running, open $ htop 
# The OS scheduler will assign its own memory space and one core to each process
# The GIL is not an issue as they are processes, each one runs Python bytecode at the same time
# Result: parallelism and speedup, the app will take just the time of the longest process, not the sum of all them

import time
import multiprocessing
 
# Calculates and prints a specific number in the Fibonacci sequence
# The classic way to generate heavy and sustained CPU load
# Uses nested functions and recursion
def print_fib(number):                                # Outer function: takes the input and prints the output
    def fib(n):                                       # Nested function: can only be called from print_fib()
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)            # Recursion: the function definition calls itself
 
    print(f"Number {number} in the Fibonacci sequence is {fib(number):,}") # Format the integer with commas for thousands separators. Python doesn't support dots for thousands separators.

     
def fibonacci_process_forty_code():
    # Defines the work for this process
    print_fib(50)
 
def fibonacci_process_fortyone_code():
    # Defines the work for this process
    print_fib(51)

def fibonacci_process_fortytwo_code():
    # Defines the work for this process
    print_fib(52)
 
def fibonacci_process_fortythree_code():
    # Defines the work for this process
    print_fib(53) 

def fibonacci_process_fortyfour_code():
    # Defines the work for this process
    print_fib(54) 



# Main is best practice in normal scripts but mandatory in multiprocessing scripts
if __name__ == '__main__':                                   

    print("\nStarting parallel Fibonacci calculations, this might take hours")
    start_time = time.time()

    fibonacci_process_forty = multiprocessing.Process(target=fibonacci_process_forty_code)
    fibonacci_process_forty.start()
    
    fibonacci_process_fortyone = multiprocessing.Process(target=fibonacci_process_fortyone_code)
    fibonacci_process_fortyone.start()

    fibonacci_process_fortytwo = multiprocessing.Process(target=fibonacci_process_fortytwo_code)
    fibonacci_process_fortytwo.start()
        
    fibonacci_process_fortythree = multiprocessing.Process(target=fibonacci_process_fortythree_code)
    fibonacci_process_fortythree.start()

    fibonacci_process_fortyfour = multiprocessing.Process(target=fibonacci_process_fortyfour_code)
    fibonacci_process_fortyfour.start()
    
    print(f"Hello from parent process")

    # Wait until the child processes have finished before closing the parent process
    fibonacci_process_forty.join()                         
    fibonacci_process_fortyone.join() 
    fibonacci_process_fortytwo.join() 
    fibonacci_process_fortythree.join()
    fibonacci_process_fortyfour.join() 
 
    # Show time
    end_time = time.time()
    execution_time_minutes = (end_time - start_time) / 60
    print(f"Time: {execution_time_minutes:,.2f} minutes\n")

    