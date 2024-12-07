from advent import BaseSolution

from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


def cat(a: int, b: int) -> int:
    return int(str(a) + str(b))


def solve(eqs: list[tuple[int, list[int]]], *ops: Callable[[int, int], int]) -> int:
    total = 0

    for val, nums in eqs:
        res = [nums[0]]

        for b in nums[1:]:
            tmp = []

            for op in ops:
                tmp += list(map(lambda a: op(a, b), res))

            res = tmp

        if val in res:
            total += val

    return total


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[tuple[int, list[int]]]]:
        eqs = []

        for line in input.splitlines():
            val, *nums = line.split()
            eqs.append((int(val.removesuffix(":")), list(map(int, nums))))

        return (eqs,)

    def part_one_impl(self, eqs) -> int:  # type: ignore
        return solve(eqs, add, mul)

    def part_two_impl(self, eqs) -> int:  # type: ignore
        return solve(eqs, add, mul, cat)
