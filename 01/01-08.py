# First we run two IO-bound tasks sequentially
# Next we run the two IO-bound tasks concurrently using threads
# CPU-bound threads serialize due to the GIL but the I/O-bound threads release the GIL while waiting, enabling overlap (concurrency)
# Library: requests, popular library for sending HTTP requests and fetching web pages. An alternative to requests is urllib

import time
import requests
import threading
 
URL = "https://www.python.org"


# Synchronous web request
def read_example():
    response = requests.get(URL)                         # requests.get() sends the HTTP requests and blocks the app until we get the data back from the server
    print(response.status_code)
 

# Synchronously (sequential)
print()
start_time = time.time()
read_example()                                           # The main thread will be waiting until we get the data back from the server
read_example()                                           # Idem
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time, running synchronously: {execution_time_seconds:.2f} seconds\n")

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

# Concurrently, using threads
start_time = time.time()
thread_1.start()                                          # The main thread will continue, thread_1 will be active, monitoring the socket until we get the data back from the server
thread_2.start()                                          # The main thread will continue, thread_2 will be active, monitoring the socket until we get the data back from the server 
 
print('Hello from main thread. All threads running.')
 
thread_1.join()
thread_2.join()
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time, with threads: {execution_time_seconds:.2f} seconds\n")

