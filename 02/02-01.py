# Asyncio: Coroutines

import asyncio

async def coroutine_greet():
    print("Hello, world")

def greet():
    print("Hello, world")


async def coroutine_add_one(number):
    return number + 1
 
def add_one(number):
    return number + 1

print()
greet()

# Run the function
result = add_one(1)
print(f"Result 1+1: {result}")


# Try to run the coroutine (it won't work, as coroutines are not run just by entering the name as if they were normal functions)
# The code inside will not run and it will just return a coroutine object
coroutine_result = coroutine_add_one(1)
print(f"Coroutine result 1+1: {coroutine_result}")

# Tell Python to safely close it so it doesn't throw a warning when deleted
coroutine_result.close()

# Now I run the coroutine using asyncio.run()
coroutine_result = asyncio.run(coroutine_add_one(1))
print(f"Coroutine result 1+1: {coroutine_result}")

print()