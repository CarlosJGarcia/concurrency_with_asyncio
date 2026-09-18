# Asyncio: How to define a coroutine (async function) and how to call it

import asyncio

# Function
def greet():
    print("Hello, world")


# Coroutine that doesn't return any value
async def coroutine_greet():
    print("Hello, world")


# Function that returns a value
def increase(n):
    return n + 1

# Coroutine that returns a value
async def coroutine_increase(n):
    return n + 1
 


# Run the functions

print()
greet()
result = increase(1)
print(f"1 + 1 = {result}")

# Try to run the coroutine as if it were a normal function
# It won't work, as coroutines are not run just by entering the name as if they were normal functions
# The code inside will not run and it will just return a coroutine object
coroutine_result = coroutine_increase(1)
print(f"Coroutine result 1+1: {coroutine_result}")

# Close the coroutine object so Python doesn't throw a warning
coroutine_result.close()

# Run the coroutine using asyncio.run()
coroutine_result = asyncio.run(increase(1))
print(f"Coroutine 1 + 1 = {coroutine_result}")

# Run the coroutine using await is not possible here, because await is allowed only within an async function (coroutine)
# coroutine_result = await increase(42) 

print()