import multiprocessing
import time
import random
from datetime import datetime

def worker():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    print(f"The current time is: {datetime.now()}")

if __name__ == "__main__":
    processes = []
    for _ in range(3):
        myprocess = multiprocessing.Process(target=worker)
        processes.append(myprocess)
        myprocess.start()

    for myprocess in processes:
        myprocess.join()