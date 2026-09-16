import asyncio
 
async def add_one(number):
    return number + 1
 
 
async def main():
    one_plus_one = await add_one(1)     # Runs add_one() and pauses the coroutine where it is contained until add_one() finishes and returns a result
    two_plus_one = await add_one(2)     # Idem  

    print()
    print("1 + 1 =", one_plus_one)
    print("2 + 1 =", two_plus_one)
    print()
 
# Main
asyncio.run(main())