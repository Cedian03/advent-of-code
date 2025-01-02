from typing import Any
from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[Any, ...]:
        return (foo := [[int(x) for x in line] for line in input.splitlines()], len(foo[0]), len(foo))

    def part_one_impl(self, foo: str, width, height) -> int:  # type: ignore
        def rec(x, y, n, s):
            if x not in range(width):
                return

            if y not in range(height):
                return

            if foo[y][x] != n:
                return

            if foo[y][x] == 9:
                return s.add((x, y))

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rec(x + dx, y + dy, n + 1, s)

        r = 0

        for y in range(height):
            for x in range(width):
                s = set()

                rec(x, y, 0, s)

                print(f"({x}, {y}) => {s} ({len(s)})")

                r += len(s)

        return r

    def part_two_impl(self, foo, width, height) -> int:  # type: ignore
        def rec(x, y, n):
            if x not in range(width):
                return 0

            if y not in range(height):
                return 0

            if foo[y][x] != n:
                return 0

            if foo[y][x] == 9:
                return 1

            r = 0

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                r += rec(x + dx, y + dy, n + 1)

            return r

        r = 0

        for y in range(height):
            for x in range(width):
                z = rec(x, y, 0)

                print(f"({x}, {y}) => {z}")

                r += z
        return r
