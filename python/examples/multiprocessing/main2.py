import multiprocessing
import time

from utils import is_prime


if __name__ == "__main__":
    MAX_NUMBER = 1000000

    primes = []

    start = time.time()

    with multiprocessing.Pool(4) as pool:
        # imap is much slower than map
        primes = [n + 1 for n, prime in enumerate(pool.map(is_prime, range(1, MAX_NUMBER))) if prime]
        
    print(f"Found {len(primes)} prime numbers under {MAX_NUMBER} in {time.time() - start} seconds.")
