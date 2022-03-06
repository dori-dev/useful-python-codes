"""asynchronous in python
"""
import asyncio


async def factorial(number: int) -> int:
    """calculate factorial of number

    Args:
        number (int): number will calculate it factorial

    Returns:
        int: factorial of number
    """
    result = 1
    print(f"started calculate {number}")
    for i in range(1, number+1):
        result *= i
        if i % 10_000 == 0:
            await asyncio.sleep(0.1)

    print(f"finished calculate {number}")
    return result


async def main() -> list:
    """main of codes

    Returns:
        list: results
    """
    numbers = [100000, 20, 300, 1230]
    tasks = []
    for num in numbers:
        tasks.append(loop.create_task(factorial(num)))

    await asyncio.wait(tasks)
    return tasks


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(main())
        print("result:")
        results = list(map(lambda x: x.result(), results))
        print(results[1])
    except Exception as err:
        print(err)
    finally:
        loop.close()
