from advent import BaseSolution

from collections import defaultdict


class Solution(BaseSolution):
    def part_one(self) -> int:
        left: list[int] = []
        right: list[int] = []

        for line in self.input.splitlines():
            x, y = line.split()
            left.append(int(x))
            right.append(int(y))

        return sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])

    def part_two(self) -> int:
        left: list[int] = []
        right: defaultdict[int, int] = defaultdict(int)

        for line in self.input.splitlines():
            x, y = line.split()
            left.append(int(x))
            right[int(y)] += 1

        return sum([x * right[x] for x in left])
