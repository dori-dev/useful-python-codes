"""asyncio example code
"""

import asyncio


async def main():
    """main function
    """
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(1)
    print("B")
    return_value = await task
    print(return_value)


async def other_function():
    """other function
    """
    print("1")
    await asyncio.sleep(2)
    print("2")
    return "other function"

asyncio.run(main())
