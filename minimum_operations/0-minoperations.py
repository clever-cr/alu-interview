#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    buffer = 1

    while buffer < n:
        if n % buffer == 0:
            operations += 1
            buffer = n // buffer
        else:
            operations += 1
            buffer += buffer

    if buffer == n:
        return operations
    else:
        return 0
