# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Maximus Amick
# Section:      513
# Assignment:   10.15 LAB: Chocolate boxes
# Date:         25 October 2025

from functools import lru_cache
from typing import Dict, List, Tuple

_ALLOWED_DARK_COUNTS = {0, 2, 3}


def _normalize_attribute(value: str) -> str:
    return str(value).strip().lower()


def _pair_ok(a: Tuple[str, str, str, str], b: Tuple[str, str, str, str]) -> bool:
    if a == b:
        return False
    if {"square", "rectangle"} == {a[1], b[1]}:
        return False
    if {"caramel", "vanilla"} == {a[2], b[2]}:
        return False
    if {"nuts", "sprinkles"} == {a[3], b[3]}:
        return False
    return True


def _dark_balance_possible(dark_remaining: int, boxes_remaining: int) -> bool:
    if boxes_remaining == 0:
        return dark_remaining == 0
    for boxes_with_three in range(0, boxes_remaining + 1):
        rest_dark = dark_remaining - 3 * boxes_with_three
        if rest_dark < 0:
            break
        if rest_dark % 2 != 0:
            continue
        boxes_with_two = rest_dark // 2
        boxes_with_zero = boxes_remaining - boxes_with_three - boxes_with_two
        if boxes_with_zero >= 0:
            return True
    return False


def make_boxes(chocolates: Dict[int, List[str]]) -> List[List[int]]:
    """
    Partition truffles into boxes of four while satisfying the assignment constraints.
    """
    if not isinstance(chocolates, dict):
        raise TypeError("chocolates must be a dictionary")
    n = len(chocolates)
    if n == 0:
        return []
    if n % 4 != 0:
        raise ValueError("Number of truffles must be divisible by 4.")
    ids = sorted(chocolates)
    id_attrs: Dict[int, Tuple[str, str, str, str]] = {}
    for tid in ids:
        attrs = chocolates[tid]
        if not isinstance(attrs, (list, tuple)) or len(attrs) != 4:
            raise ValueError("Each truffle must have exactly four attributes.")
        normalized = tuple(_normalize_attribute(a) for a in attrs)
        id_attrs[tid] = normalized

    neighbor_sets = {tid: set() for tid in ids}
    for idx, tid in enumerate(ids):
        attrs_tid = id_attrs[tid]
        for other in ids[idx + 1 :]:
            attrs_other = id_attrs[other]
            if _pair_ok(attrs_tid, attrs_other):
                neighbor_sets[tid].add(other)
                neighbor_sets[other].add(tid)

# Comment
    is_dark = {tid: id_attrs[tid][0] == "dark" for tid in ids}

    @lru_cache(maxsize=None)
    def solve(unused_tuple: Tuple[int, ...]) -> Tuple[Tuple[int, ...], ...] | None:
        if not unused_tuple:
            return ()
        if len(unused_tuple) % 4 != 0:
            return None
        boxes_remaining = len(unused_tuple) // 4
        unused_set = set(unused_tuple)
        dark_remaining = sum(1 for tid in unused_tuple if is_dark[tid])
        if not _dark_balance_possible(dark_remaining, boxes_remaining):
            return None

        neighbors_in_unused = {}
        candidate_tid = None
        min_degree = None
        for tid in unused_tuple:
            available = neighbor_sets[tid].intersection(unused_set)
            neighbors_in_unused[tid] = available
            degree = len(available)
            if degree < 3:
                return None
            if (
                min_degree is None
                or degree < min_degree
                or (degree == min_degree and tid < candidate_tid)
            ):
                min_degree = degree
                candidate_tid = tid
        assert candidate_tid is not None

        available_neighbors = sorted(neighbors_in_unused[candidate_tid])
        combo_candidates: List[Tuple[int, Tuple[int, ...], int]] = []
        count_neighbors = len(available_neighbors)
        for i in range(count_neighbors):
            a = available_neighbors[i]
            for j in range(i + 1, count_neighbors):
                b = available_neighbors[j]
                if b not in neighbors_in_unused[a]:
                    continue
                for k in range(j + 1, count_neighbors):
                    c = available_neighbors[k]
                    if c not in neighbors_in_unused[a] or c not in neighbors_in_unused[b]:
                        continue
                    quad = tuple(sorted((candidate_tid, a, b, c)))
                    quad_dark = sum(1 for t in quad if is_dark[t])
                    if quad_dark not in _ALLOWED_DARK_COUNTS:
                        continue
                    score = sum(len(neighbors_in_unused[t]) for t in quad)
                    combo_candidates.append((score, quad, quad_dark))

        if not combo_candidates:
            return None

        combo_candidates.sort(key=lambda item: (item[0], item[1]))
        for _, quad, quad_dark in combo_candidates:
            next_unused_set = unused_set - set(quad)
            if not _dark_balance_possible(
                dark_remaining - quad_dark, len(next_unused_set) // 4
            ):
                continue
            sub_solution = solve(tuple(sorted(next_unused_set)))
            if sub_solution is not None:
                return (quad,) + sub_solution
        return None

    solution = solve(tuple(ids))
    if solution is None or len(solution) != n // 4:
        solve.cache_clear()
        raise ValueError("Unable to construct valid boxes with given constraints.")

    boxes = [list(box) for box in solution]
    for box in boxes:
        box.sort()
    boxes.sort()
    solve.cache_clear()
    return boxes
