# Fetch HTML page example.com and save the HTTP header as headers.txt
# Example I/O-bound task that blocks the Python script until it has been completed

import time
import urllib3
import requests
from rich.console import Console

URL = "https://www.python.org"
FILE = "headers.txt"

# Suppress the warning that prints when you disable verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

console = Console()
start_time = time.time()
console.print(f"\nLoading {URL}", style="gold1", highlight=False)
# Sends the HTTP GET request to the web server and get the whole response in an object 
response = requests.get(URL, verify=False)

# from response.headers, I get the size of the HTTP reply 
content_length_bytes = int(response.headers.get('Content-Length', 0))
content_lenght_kb = content_length_bytes / 1024
print(f"Payload size: {content_lenght_kb:.2f} KB")

# response.headers is a dictionary and items() is a method of that dictionary
# items() returns a 'dictionary view' which is easily iterable
items = response.headers.items()

# Using the return of the for loop (key and header in items), we build a list of strings. Each string has the format "{key}: {header}"
headers = [f"{key}: {header}" for key, header in items]

# Build a string, concatenating all the strings in the list, separated by \n
formatted_headers = '\n'.join(headers)

# Opens a file for writing and writes the string
print(f"Writing {FILE}")
with open(FILE, 'w') as file:
    file.write(formatted_headers)      

# Show time
end_time = time.time()
execution_time_seconds = (end_time - start_time)
console.print(f"Time: {execution_time_seconds:.2f} seconds\n", style="cyan", highlight=False)
