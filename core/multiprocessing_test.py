import time
from multiprocessing import Process, Queue
from queue import Empty


def process_some_data(q: Queue):
    for i in range(5):
        print(f"Processing number {i}...")
        time.sleep(5)
        q.put(i)
        print("Processed!")


def storing_data(q: Queue):
    while True:
        try:
            num = q.get(timeout=6)
            if num is None:
                print("Received shutdown signal.")
                break
            print(f"Storing data {num}...")
            time.sleep(3)
            print("Data stored!")
        except Empty:
            print("No data received in 6 seconds. Shutting down.")
            break


def main():
    q = Queue()
    p1 = Process(target=process_some_data, args=(q,))
    p2 = Process(target=storing_data, args=(q,))
    p1.start(); p2.start()


if __name__ == "__main__":
    main()
