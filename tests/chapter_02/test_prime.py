"""Tests for prime-finding algorithms in prime.py."""

from algo.chapters.chapter_02_complexity_primes.prime import prime1, prime2, prime3

PRIMES_UP_TO_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_prime1_known_primes() -> None:
    """prime1 returns correct primes up to 30."""
    primes, _ = prime1(30)
    assert primes == PRIMES_UP_TO_30


def test_prime2_known_primes() -> None:
    """prime2 returns correct primes up to 30."""
    primes, _ = prime2(30)
    assert primes == PRIMES_UP_TO_30


def test_prime3_known_primes() -> None:
    """prime3 returns correct primes up to 30."""
    primes, _ = prime3(30)
    assert primes == PRIMES_UP_TO_30


def test_all_three_agree() -> None:
    """All three algorithms produce the same prime list."""
    p1, _ = prime1(200)
    p2, _ = prime2(200)
    p3, _ = prime3(200)
    assert p1 == p2 == p3


def test_prime1_edge_small() -> None:
    """prime1 with maximum=4 returns [2, 3]."""
    primes, _ = prime1(4)
    assert primes == [2, 3]


def test_prime2_edge_small() -> None:
    """prime2 with maximum=2 returns [2]."""
    primes, _ = prime2(2)
    assert primes == [2]


def test_prime3_edge_small() -> None:
    """prime3 with maximum=2 returns [2]."""
    primes, _ = prime3(2)
    assert primes == [2]
