#!/usr/bin/env python3
"""
minimum operation file
"""


def minOperations(n: int) -> int:
    """ A method that calculates the fewest
        number of operations needed to result
        in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0
    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
