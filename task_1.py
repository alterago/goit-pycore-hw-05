"""Task 1: Fibonacci numbers with a cache kept in a closure."""

from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """Return a fibonacci(n) function that caches computed values."""
    # The cache lives in the enclosing scope, so it persists between calls.
    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """Return the n-th Fibonacci number, computing it recursively once."""
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    # Get the fibonacci function
    fib = caching_fibonacci()

    # Use it to compute Fibonacci numbers
    print(fib(10))  # 55
    print(fib(15))  # 610
