# Program that sleeps for 1 second and then prints a "hello, world" message

import asyncio
 
async def message():
    await asyncio.sleep(5)     # Simulates a IO-Bound task, for example a LLM inference request or a SQL query that takes 1 second             
    return "Hello, world"


async def main():
    print()
    msg = await message()
    print(f"{msg}\n")
 
# Main
asyncio.run(main())