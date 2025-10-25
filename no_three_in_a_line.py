# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   10.14 LAB: No three in a line
# Date:         24 October 2025

from math import gcd
import random


def _normalize_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    A = y1 - y2
    B = x2 - x1
    C = x1 * y2 - x2 * y1
    g = gcd(abs(A), abs(B))
    g = gcd(g, abs(C))
    if g == 0:
        g = 1
    A //= g
    B //= g
    C //= g
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return (A, B, C)


def _can_add(point, selected, forbidden_lines):
    for existing in selected:
        if _normalize_line(point, existing) in forbidden_lines:
            return False
    return True


def _register_lines(point, selected, forbidden_lines):
    for existing in selected:
        forbidden_lines.add(_normalize_line(point, existing))


def _greedy_build(order, target):
    selected = []
    forbidden_lines = set()
    for point in order:
        if _can_add(point, selected, forbidden_lines):
            _register_lines(point, selected, forbidden_lines)
            selected.append(point)
            if len(selected) >= target:
                break
    return selected


def _search_layout(points_pool, n, target):
    best = []
    max_attempts = max(200, n * 10)
    deterministic_orders = [
        sorted(points_pool),
        sorted(points_pool, key=lambda p: (p[1], p[0])),
        sorted(points_pool, key=lambda p: ((p[0] + p[1]) % n, p[0], p[1])),
        sorted(points_pool, key=lambda p: ((p[0] - p[1]) % n, p[0], p[1])),
    ]
    attempts = 0
    for order in deterministic_orders:
        attempts += 1
        layout = _greedy_build(order, target)
        if len(layout) > len(best):
            best = layout
        if len(layout) >= target:
            return layout
    rng = random.Random(7919 * n + 104729 * target)
    while attempts < max_attempts:
        attempts += 1
        order = points_pool[:]
        rng.shuffle(order)
        layout = _greedy_build(order, target)
        if len(layout) > len(best):
            best = layout
        if len(layout) >= target:
            return layout
    return best

# ChatGPT-5-Codex (preview) wrote this code lol
def no_three_in_line(n):
    if n <= 0:
        return []

    points_pool = [(x, y) for x in range(n) for y in range(n)]
    targets_raw = [min(2 * n, n * n), int(1.9 * n), int(1.8 * n), int(1.7 * n), n]
    targets = []
    for value in targets_raw:
        value = max(n, min(int(value), n * n))
        if value not in targets:
            targets.append(value)

    best_layout = []
    for target in targets:
        layout = _search_layout(points_pool, n, target)
        if len(layout) > len(best_layout):
            best_layout = layout
        if len(layout) >= target:
            break

    if len(best_layout) < n:
        best_layout = _search_layout(points_pool, n, n)

    best_layout.sort()
    return [[x, y] for x, y in best_layout]


if __name__ == "__main__":
    n = 8
    points = no_three_in_line(n)
    print(points)
