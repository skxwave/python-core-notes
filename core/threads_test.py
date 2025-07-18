import threading
import time
import random


def log_metrics():
    while True:
        time.sleep(5)
        print("[Logger] CPU: 10%, Mem: 42%")


# t = threading.Thread(
#     target=log_metrics,
#     daemon=True, # When main program ends - daemon thread also ends
# )
# t.start()

# while True:
#     time.sleep(1)
#     print("[Main] Doing something important...")


from concurrent.futures import ThreadPoolExecutor
import time


def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    print(f"Task {n} done")


# with ThreadPoolExecutor(max_workers=3) as pool:
#     pool.map(task, (1, 2, 3, 4, 5, 6))

import requests


def download(url):
    print(f"Starting {url}")
    r = requests.get(url)
    print(f"{url} — done: {len(r.content)} bytes")


urls = [
    "https://httpbin.org/bytes/100000",
    "https://httpbin.org/bytes/200000",
    "https://httpbin.org/bytes/300000",
]

# threads = [threading.Thread(target=download, args=(url,)) for url in urls]

# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

# print("All downloads complete")

# ---
# Few Threads testing
# ---

def some_task():
    # time.sleep(2)
    current_time = time.time()
    print(f"Done; {current_time}")

thread1 = threading.Thread(
    target=some_task,
    name="thread1",
)
thread2 = threading.Thread(
    target=some_task,
    name="thread2",
)
thread3 = threading.Thread(
    target=some_task,
    name="thread3",
)
thread4 = threading.Thread(
    target=some_task,
    name="thread4",
)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
