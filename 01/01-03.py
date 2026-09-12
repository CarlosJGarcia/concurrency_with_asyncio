# Multithreaded Python application
# Shows the PID of the process and the names of the threads
# Libraries: os and threading

import os
import threading


# Define a function that says hello and shows the current thread id. For this to work well, all has to be in the same print line 
def hello_from_thread():
    print(f"--> hello, thread\n--> The current thread is {threading.current_thread().name}\n")
    

# main
print(f"\nhello, world")
print(f"Python process running with process id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f"Python is currently running {total_threads} thread(s)")
print(f"The current thread is {thread_name}\n")

hello_thread = threading.Thread(target=hello_from_thread)           # initializes a new thread object, pointing to the function     
hello_thread.start()                                                # Start running hello_thread
 
total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f"Python is currently running {total_threads} thread(s)")
print(f"The current thread is {thread_name}\n")
 
hello_thread.join()                                                 # Wait until hello_thread has finished to close the Main Thread and the Process