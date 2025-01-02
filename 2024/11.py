from typing import Any
from advent import BaseSolution

from collections import defaultdict, Counter


def solution(stones: list[int], n: int):
    counter = dict(Counter(stones))

    for i in range(n):
        new_counter = defaultdict(int)

        for k, v in counter.items():
            if k == 0:
                new_counter[1] += v
            elif len(s := str(k)) % 2 == 0:
                new_counter[int(s[: len(s) // 2])] += v
                new_counter[int(s[len(s) // 2 :])] += v
            else:
                new_counter[k * 2024] += v

            counter = new_counter

    return sum(counter.values())


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[Any, ...]:
        return ([int(x) for x in input.split()],)

    def part_one_impl(self, stones: list[int]) -> int:  # type: ignore
        return solution(stones, 25)

    def part_two_impl(self, stones: list[int]) -> int:  # type: ignore
        return solution(stones, 75)
