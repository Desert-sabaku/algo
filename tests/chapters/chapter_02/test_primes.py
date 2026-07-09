"""Tests for the Sieve of Eratosthenes in primes.py."""

from algo.chapters.chapter_02_complexity_primes.prime import prime2
from algo.chapters.chapter_02_complexity_primes.primes import sieve


def test_sieve_10() -> None:
    """sieve(10) marks exactly the primes up to 9."""
    result = sieve(10)
    assert result[2] is True
    assert result[3] is True
    assert result[5] is True
    assert result[7] is True
    assert result[0] is False
    assert result[1] is False
    assert result[4] is False
    assert result[6] is False
    assert result[8] is False
    assert result[9] is False


def test_sieve_empty() -> None:
    """sieve(0) returns an empty list."""
    assert sieve(0) == []


def test_sieve_two() -> None:
    """sieve(2) marks only index 0 as non-prime."""
    result = sieve(2)
    assert result[0] is False
    assert result[1] is False


def test_sieve_cross_check_prime2() -> None:
    """Primes from sieve match those from prime2."""
    limit = 50
    sieve_primes = [i for i, v in enumerate(sieve(limit)) if v]
    prime2_primes, _ = prime2(limit)
    assert sieve_primes == prime2_primes
