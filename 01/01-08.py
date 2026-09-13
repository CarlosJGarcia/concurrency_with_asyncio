import time
import requests
import threading
 
URL = "https://www.python.org"

def read_example():
    response = requests.get(URL)
    print(response.status_code)
 

# Synchronously (sequential)
print()
start_time = time.time()
read_example()
read_example()
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time, running synchronously: {execution_time_seconds:.2f} seconds\n")

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

# Asynchronously (concurrent) 
start_time = time.time()
thread_1.start()
thread_2.start()
 
print('Hello from main thread. All threads running.')
 
thread_1.join()
thread_2.join()
 
# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
print(f"Time, with threads: {execution_time_seconds:.2f} seconds\n")

