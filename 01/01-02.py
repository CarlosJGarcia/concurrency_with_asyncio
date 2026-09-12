# Single-thread Python application
# Show the PID and thread name
# Libraries: os and threading

import os
import threading
 
print()
print("hello, world")
print(f"Python process running with process id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name
print(f"Python is currently running {total_threads} thread(s)")
print(f"The current thread is {thread_name}\n")