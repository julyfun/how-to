import multiprocessing
import time

from utils import is_prime

MAX_NUMBER = 1000000
primes = []
def worker(inq, outq):
    while val := inq.get():
        start, end = val
        primes = []
        for n in range(start, end):
            if is_prime(n):
                primes.append(n)
        outq.put(primes)
    outq.put(None)
    
if __name__ == "__main__":
    multiprocessing.freeze_support()
    start = time.time()
    inq = multiprocessing.Queue()
    outq = multiprocessing.Queue()

    workers = [multiprocessing.Process(target=worker, args=(inq, outq)) for _ in range(4)]

    for w in workers:
        w.start()

    for i in range(4):
        inq.put((i * MAX_NUMBER // 4, (i + 1) * MAX_NUMBER // 4))
    for _ in range(4):
        inq.put(None)

    finish = 0
    while finish < 4:
        if n := outq.get():
            primes.extend(n)
        else: # got None
            finish += 1

    print(f"Took {time.time() - start} seconds")
    print(f"Got {len(primes)} primes")
