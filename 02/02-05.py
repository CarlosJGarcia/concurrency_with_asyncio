# Create two tasks and run them at the same time
import os
import sys
import asyncio

# Point Python to the folder one level up, named "util" so "from delay_functions" works
import_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../util'))
if import_dir not in sys.path:
    sys.path.insert(0, import_dir)

from delay_functions import delay
 
 
async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)
 
asyncio.run(main())

