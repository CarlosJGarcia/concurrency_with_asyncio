
# A basic event loop

from collections import deque

def process_message(message):
    print(f"Processing: {message}")

messages = deque()
 
while True:
    if messages:
        message = messages.pop()
        process_message(message)