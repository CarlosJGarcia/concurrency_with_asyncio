# Create two tasks and run them concurrently

import asyncio

async def delayincrease(seconds):
    print(f'sleeping for {seconds} second(s)')
    await asyncio.sleep(seconds)
    print(f'finished sleeping for {seconds} second(s)')
    return seconds + 1

  
async def main():

    # Create a task for the coroutine (task -> coroutine -> code that otherwise would be in a function)
    print("\nCreating the tasks")
    delay_task = asyncio.create_task(delayincrease(3))
    delay_again_task = asyncio.create_task(delayincrease(4))

    # Execute the tasks
    print("\nExecuting the tasks concurrently")
    result_one = await delay_task
    result_two = await delay_again_task

    print(f"\nReturn from delayincrease(3): {result_one}")
    print(f"Return from delayincrease(4): {result_two}\n")


# Main  
asyncio.run(main())

