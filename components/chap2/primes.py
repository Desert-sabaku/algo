import cProfile


def sieve(limit: int) -> list[bool]:
    """Returns a list of natural numbers up to the specified number, having filtered out composite numbers.

    Args:
        limit (int): the specified number

    Returns:
        list[bool]: List of the prime numbers
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

    def task(limit: int) -> list[bool]:
        return sieve(limit)

    LIMIT = 10000000
    cProfile.run("task(LIMIT)")
    # print([i for i, e in enumerate(task(LIMIT)) if e])
