# Create a task and run it
import os
import sys
import asyncio

# Point Python to the folder one level up, named "util" so "from delay_functions" works
import_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../util'))
if import_dir not in sys.path:
    sys.path.insert(0, import_dir)

from delay_functions import delay
  
async def main():

    # Create a task for the coroutine (task -> coroutine -> code that otherwise would be in a function)
    print("\nCreating the task")
    delay_task = asyncio.create_task(delay(3))
    print(f"Type of the task object: {type(delay_task)}\n")

    # Execute the task
    result = await delay_task
    print(f"Return value from running delay(3) asycronously: {result}\n")


# Main  
asyncio.run(main())

