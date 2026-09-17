import os
import sys
import asyncio

# Point Python to the folder one level up, named "util" so "from delay_functions" works
import_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../util'))
if import_dir not in sys.path:
    sys.path.insert(0, import_dir)

from delay_functions import delay
 

async def add_one(number):
    return number + 1
 
async def message():
    await delay(2)                     # Simulates a IO-Bound task, for example a LLM inference request or a SQL query that takes 1 second             
    return "Hello, world"
 
async def main():
    print()
    msg = await message()              # Pauses main() until message() returns
    one_plus_one = await add_one(1)    # Pauses main() until add_one() returns      

    print(f"\n{msg}")
    print(f"1 + 1 = {one_plus_one}\n")
    
 
asyncio.run(main())