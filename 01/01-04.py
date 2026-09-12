# Multiprocess Python application
# Libraries: os and multiprocessing

import os
import multiprocessing

 
def hello_from_process():
    print(f"--> Hello from child process {os.getpid()}\n")

if __name__ == '__main__':                                               # Main is best practice in normal scripts but mandatory in multiprocessing scripts

    print(f"\nHello from parent process {os.getpid()}")

    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"Goodbye from parent process {os.getpid()}\n")                # Due to race condition this *might* show before the message from the child

    hello_process.join()                                                 # Wait until the child process has finished to close the parent process

    