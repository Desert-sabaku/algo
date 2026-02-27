import cProfile


def sieve(limit: int) -> list[bool]:
    """Returns a boolean sieve marking prime indices up to but not including limit.

    Args:
        limit (int): The exclusive upper bound for the sieve.

    Returns:
        list[bool]: A list where index i is True if i is prime, False otherwise.
    """
    primes = [True] * limit
    if limit > 0:
        primes[0] = False
    if limit > 1:
        primes[1] = False

    for i in range(2, limit):
        if i * i >= limit:
            break
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False

    return primes


if __name__ == "__main__":
    LIMIT = 10000000
    cProfile.run("sieve(LIMIT)")
    # print([i for i, e in enumerate(task(LIMIT)) if e])
