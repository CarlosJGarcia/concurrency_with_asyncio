# Fetch HTML page example.com and save the HTTP header as headers.txt
# Example I/O-bound task that blocks the Python script until it has been completed

import time
import urllib3
import requests
from rich.console import Console

URL = "https://www.roche.com"
FILE = "headers.txt"

console = Console()

# Suppress the obnoxious warning that prints when you disable verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Sends the HTTP GET request to the web server and get the whole response in an object 
#response = requests.get('https://www.example.com', verify=False)

start_time = time.time()
console.print(f"\nLoading {URL}", style="gold1", highlight=False)
response = requests.get(URL, verify=False)

# response = requests.get('https://www.elpais.es', verify=False)

# response.headers is a dictionary and items() is a method of that dictionary
# items() returns a 'dictionary view' which is easily iterable
items = response.headers.items()

# Using the return of the for loop (key and header in items), we build a list of strings. Each string has the format "{key}: {header}"
headers = [f"{key}: {header}" for key, header in items]

# Build a string, concatenating all the strings in the list, separated by \n
formatted_headers = '\n'.join(headers)

# Opens a file for writing and writes the string
console.print(f"Writing {FILE}", style="gold1", highlight=False)
with open(FILE, 'w') as file:
    file.write(formatted_headers)      

end_time = time.time()
execution_time_seconds = (end_time - start_time)
console.print(f"Time: {execution_time_seconds:.2f} seconds\n", style="cyan", highlight=False)
