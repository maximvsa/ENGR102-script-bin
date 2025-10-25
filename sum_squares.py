# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   10.13 LAB: Sum squares
# Date:         24 October 2024

from time import time

def list_nums(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    limit = int(n ** 0.5)
    two_square = {}
    for c in range(limit + 1):
        c_sq = c * c
        if c_sq > n:
            break
        for d in range(c, limit + 1):
            total = c_sq + d * d
            if total > n:
                break
            if total not in two_square:
                two_square[total] = (c, d)
    for a in range(limit + 1):
        a_sq = a * a
        if a_sq > n:
            break
        for b in range(a, limit + 1):
            total = a_sq + b * b
            if total > n:
                break
            remainder = n - total
            if remainder in two_square:
                c, d = two_square[remainder]
                return [a, b, c, d]
    return None

def count_sets(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    limit = int(n ** 0.5)
    two_square = {}
    for c in range(limit + 1):
        c_sq = c * c
        if c_sq > n:
            break
        for d in range(c, limit + 1):
            total = c_sq + d * d
            if total > n:
                break
            two_square.setdefault(total, []).append((c, d))
    unique_sets = set()
    for a in range(limit + 1):
        a_sq = a * a
        if a_sq > n:
            break
        for b in range(a, limit + 1):
            total = a_sq + b * b
            if total > n:
                break
            remainder = n - total
            for c, d in two_square.get(remainder, []):
                unique_sets.add(tuple(sorted((a, b, c, d))))
    return len(unique_sets)

# how to measure how long your function takes to run:
t1 = time() # get start time
print(list_nums(99999)) # run function
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result