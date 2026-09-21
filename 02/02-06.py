# Create two tasks and run them concurrently
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
    print("\nCreating the tasks")
    delay_task = asyncio.create_task(delay(3))
    delay_again_task = asyncio.create_task(delay(4))

    # Execute the tasks
    print("\nExecuting the tasks")
    result_one = await delay_task
    result_two = await delay_again_task

    print(f"\nReturn value from running delay(3) asycronously: {result_one}")
    print(f"Return value from running delay(4) asycronously: {result_two}\n")


# Main  
asyncio.run(main())

