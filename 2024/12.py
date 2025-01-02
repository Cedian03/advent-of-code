from typing import Any
from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[Any, ...]:
        return (foo := [line for line in input.splitlines()], len(foo[0]), len(foo))

    def part_one_impl(self, foo: list[str], width: int, height: int) -> int:  # type: ignore
        v = set()

        def rec(x: int, y: int, c: str, a: list[tuple[int, int]], f: list[tuple[int, int]]):
            if x not in range(width):
                f.append((x, y))
                return

            if y not in range(height):
                f.append((x, y))
                return

            if foo[y][x] != c:
                f.append((x, y))
                return

            if (x, y) in a:
                return

            a.append((x, y))
            v.add((x, y))

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                rec(x + dx, y + dy, c, a, f)

        r = 0

        for y in range(height):
            for x in range(width):
                if (x, y) not in v:
                    a = list()
                    b = list()

                    rec(x, y, foo[y][x], a, b)

                    a = set(a)

                    r += len(a) * len(b)

        return r

    def part_two_impl(self, foo: list[str], width: int, height: int) -> int:  # type: ignore
        v = set()

        def rec(x: int, y: int, c: str, a: list[tuple[int, int]], f: set[tuple[int, int, int, int]]):
            if (x, y) in a:
                return

            a.append((x, y))
            v.add((x, y))

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy

                if nx not in range(width) or ny not in range(height) or foo[ny][nx] != c:
                    f.add((nx, ny, dx, dy))
                else:
                    rec(nx, ny, c, a, f)

        r = 0

        for y in range(height):
            for x in range(width):
                if (x, y) not in v:
                    a = list()
                    b = set()

                    rec(x, y, foo[y][x], a, b)

                    a = set(a)

                    i = 0

                    while b:
                        sx, sy, dx, dy = b.pop()

                        if dx == 0:  # Horizontal
                            xx = sx + 1

                            while (xx, sy, dx, dy) in b:
                                b.remove((xx, sy, dx, dy))
                                xx += 1

                            xx = sx - 1

                            while (xx, sy, dx, dy) in b:
                                b.remove((xx, sy, dx, dy))
                                xx -= 1
                        else:
                            yy = sy + 1

                            while (sx, yy, dx, dy) in b:
                                b.remove((sx, yy, dx, dy))
                                yy += 1

                            yy = sy - 1

                            while (sx, yy, dx, dy) in b:
                                b.remove((sx, yy, dx, dy))
                                yy -= 1

                        i += 1

                    print(f"{foo[y][x]}: {len(a)} * {i}")

                    r += len(a) * i

        return r
