# Multithreaded Python application

import os
import threading

 
def hello_from_thread():
    print(f"--> Hello from thread {threading.current_thread()}!")
 
print(f"\nHello world!")
print(f"Python process running with process id: {os.getpid()}")

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()                                                # Start running hello_thread
 
total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f"Python is currently running {total_threads} thread(s)")
print(f"The current thread is {thread_name}\n")
 
hello_thread.join()                                                 # Wait until hello_thread has finished