# This script shows the basic syntax of coroutines
import asyncio
 
async def add_one(number):
    return number + 1
 
 
# Couroutine that orchestrates the program
async def main():
    # Run add_one(1) and add_one(2) one after the other and get the result
    one_plus_one = await add_one(1)     # Runs add_one() and pauses the coroutine where it is contained (main()) until add_one() finishes and returns a result
    two_plus_one = await add_one(2)     # Idem  

    print()
    print("1 + 1 =", one_plus_one)
    print("2 + 1 =", two_plus_one)
    print()
 
# Main
asyncio.run(main())