"""Task 2: find income numbers in a text with a generator and sum them."""

import re
from decimal import Decimal
from typing import Callable, Iterator

# A real number surrounded by spaces on both sides, e.g. " 1000.01 ".
NUMBER_PATTERN = re.compile(r"(?<= )\d+(?:\.\d+)?(?= )")


def generator_numbers(text: str) -> Iterator[float]:
    """Yield every real number in the text that has a space on both sides."""
    for match in NUMBER_PATTERN.finditer(text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """Return the total of the numbers that ``func`` finds in the text.

    The sum is done in Decimal so that 1000.01 + 27.45 + 324.00 gives exactly
    1351.46 instead of a float with a rounding tail.
    """
    total = sum((Decimal(str(number)) for number in func(text)), Decimal("0"))
    return float(total)


if __name__ == "__main__":
    text = (
        "The employee's total income consists of several parts: "
        "1000.01 as the main income, supplemented by additional receipts of "
        "27.45 and 324.00 dollars."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Total income: {total_income}")
