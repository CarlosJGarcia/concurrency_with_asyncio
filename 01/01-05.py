# Generating and timing the Fibonacci sequence
# Single-thread Python application
# While it's running open $ htop to see how one core will be 100% busy

import time
 
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
 
 
def fibonacci_no_threading():
    print_fib(40)
    print_fib(41)
 
 
"""
print()
for n in range(1, 7):
    print_fib(n)
"""

print("\nStarting 40 and 41")
start_time = time.time()
fibonacci_no_threading()
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time: {execution_time_seconds:.2f} seconds\n")