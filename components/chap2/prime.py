import cProfile


def prime1(maximum: int) -> tuple[list[int], int]:
    counter = 0
    primes = [2, 3]

    for candidate in range(5, maximum, 2):
        is_prime = True
        for divisor in primes[1:]:
            if divisor * divisor > candidate:
                break
            counter += 2
            if candidate % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)
            counter += 1

    return primes, counter


def prime2(maximum: int) -> tuple[list[int], int]:
    primes = [2]
    counter = 0

    for candidate in range(2, maximum + 1):
        for divisor in primes:
            counter += 1
            if candidate % divisor == 0:
                break
        else:
            primes.append(candidate)

    return primes, counter


def prime3(maximum: int) -> tuple[list[int], int]:
    primes: list[int] = []
    counter = 0

    for candidate in range(2, maximum + 1):
        for divisor in range(2, candidate):
            counter += 1
            if candidate % divisor == 0:
                break
        else:
            primes.append(candidate)

    return primes, counter


if __name__ == "__main__":
    LIMIT = 1000
    cProfile.run("prime1(LIMIT)")
    cProfile.run("prime2(LIMIT)")
    cProfile.run("prime3(LIMIT)")

    # print(*prime1(LIMIT), *prime2(LIMIT), *prime3(LIMIT), sep="\n")
