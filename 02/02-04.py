import os
import sys
import asyncio

# Point Python to the folder one level up, named '05' so "from p05_04, from p05_10 and from gpt_download" work
import_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../util'))
if import_dir not in sys.path:
    sys.path.insert(0, import_dir)

from delay_functions import delay
 
async def add_one(number: int) -> int:
    return number + 1
 
async def hello_world_message() -> str:
    await delay(1)
    return "Hello World!"
 
async def main() -> None:
    message = await hello_world_message()    
    one_plus_one = await add_one(1)          
    print(one_plus_one)
    print(message)
 
asyncio.run(main())