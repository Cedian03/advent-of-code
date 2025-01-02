from collections import defaultdict
from typing import Any
from advent import BaseSolution


from enum import StrEnum


class Enum(StrEnum):
    Wall = "#"
    Path = "."


class Node:
    g: int
    f: int

    nbors: list

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

        self.g = float("inf")
        self.f = float("inf")


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[Any, ...]:
        lines = iter(input.splitlines())

        sx = sy = ex = ey = None

        mat = []
        for y, line in enumerate(lines):
            row = []

            for x, char in enumerate(line):
                match char:
                    case "S":
                        sx, sy = x, y
                        row.append(Enum.Path)
                    case "E":
                        ex, ey = x, y
                        row.append(Enum.Path)
                    case _:
                        row.append(Enum(char))
            mat.append(row)

        assert sx is not None
        assert ex is not None

        return (mat, sx, sy, ex, ey)

    def part_one_impl(self, mat, sx, sy, ex, ey) -> int:  # type: ignore
        s = sx, sy
        e = ex, ey
        d = 0, 1

        def h(x: int, y: int) -> int:
            return abs(ex - x) + abs(ey - y)

        q = set([(*s, *d)])

        g_score = defaultdict(lambda: float("inf"))
        g_score[(*s, *d)] = 0

        f_score = defaultdict(lambda: float("inf"))
        f_score[(*s, *d)] = h(sx, sy)

        while q:
            v = vx, vy, vdx, vdy = min(q, key=lambda v: f_score[v])
            q.remove(v)

            if (vx, vy) == e:
                return g_score[v]

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                u = ux, uy, udx, udy = vx + dx, vy + dy, dx, dy

                if mat[uy][ux] == Enum.Wall:
                    continue

                alt = g_score[v] + (1 if (udx == vdx and udy == vdy) else 1001)  # TODO
                if alt < g_score[u]:
                    g_score[u] = alt
                    f_score[u] = alt + h(ux, uy)

                    if u not in q:
                        q.add(u)

    def part_two_impl(self, mat, sx, sy, ex, ey) -> int:  # type: ignore
        s = sx, sy
        e = ex, ey
        d = 0, 1

        def h(x: int, y: int) -> int:
            return abs(ex - x) + abs(ey - y)

        q = set([(*s, *d)])

        g_score = defaultdict(lambda: float("inf"))
        g_score[(*s, *d)] = 0

        f_score = defaultdict(lambda: float("inf"))
        f_score[(*s, *d)] = h(sx, sy)

        while q:
            v = vx, vy, vdx, vdy = min(q, key=lambda v: f_score[v])
            q.remove(v)

            if (vx, vy) == e:
                return g_score[v]

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                u = ux, uy, udx, udy = vx + dx, vy + dy, dx, dy

                if mat[uy][ux] == Enum.Wall:
                    continue

                alt = g_score[v] + (1 if (udx == vdx and udy == vdy) else 1001)  # TODO
                if alt < g_score[u]:
                    g_score[u] = alt
                    f_score[u] = alt + h(ux, uy)

                    if u not in q:
                        q.add(u)
