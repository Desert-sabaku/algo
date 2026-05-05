"""Smoke tests to verify the test harness is configured correctly."""

from algo.chapters.chapter_02_complexity_primes.prime import prime1
from algo.chapters.chapter_06_sorting.sort import bubble_sort


def test_imports() -> None:
    """Verify key modules can be imported."""
    assert prime1(10)[0] == [2, 3, 5, 7]
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
