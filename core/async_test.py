import asyncio


async def func1():
    print("Doing some shit on background")
    await asyncio.sleep(2)
    print("Did some shit on background in 2 secs")
    return "World!"


async def func2():
    world = asyncio.create_task(func1())
    print(f"hello")
    await asyncio.sleep(2.01)
    print(f"hello after 2 secs")


# asyncio.run(func2())


"""
Race conditions
"""

counter = 0
lock = asyncio.Lock()


async def increment():
    # We will use lock, to lock this function, so firstly it will be finished, and then the same func will run
    async with lock:
        global counter
        temp = counter
        """
        Simulating delay. Because of this `await`, the event loop takes next task and
        this next task will use counter with value 0, so we have this race condition.
        """
        await asyncio.sleep(0.1)
        counter = temp + 1
        print(counter)


async def test_func():
    print("doin something...")


# async def main():
#     await asyncio.gather(
#         increment(),
#         increment(),
#         increment(),
#         test_func(),
#     )

#     print("Final counter:", counter)


# asyncio.run(main())

queue = asyncio.Queue()


async def producer():
    for i in range(5):
        await queue.put(i)
        print(f"Produced: {i}")
    await queue.put([1, 2, 3])


async def consumer():
    await asyncio.sleep(2)
    for item in list(queue._queue):
        # queue.get()
        print(item)
        # queue.task_done()


async def main():
    await asyncio.gather(
        producer(),
        consumer()
    )


# asyncio.run(main())

event = asyncio.Event()

async def waiter():
    print("Waiting for event to be set...")
    print(f"Current status: {event.is_set()}") # False
    await event.wait()
    print(f"Event received! Current status: {event.is_set()}") # True
    event.clear()
    print(f"Event cleared. Current status: {event.is_set()}") # False


async def trigger():
    await asyncio.sleep(2)
    event.set()


async def main():
    await asyncio.gather(
        waiter(),
        trigger()
    )

# asyncio.run(main())

semaphore = asyncio.Semaphore(2)

async def task(name):
    async with semaphore:
        print(f"{name} is running")
        await asyncio.sleep(1)
        print(f"{name} is done")

async def main():
    await asyncio.gather(*(task(f"Task-{i}") for i in range(6)))

asyncio.run(main())
