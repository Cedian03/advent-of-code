from advent import BaseSolution

import re


def solution(foo):
    r = 0

    for ax, ay, bx, by, px, py in foo:
        if swapped := ay * bx >= by * ax:
            ax, ay, bx, by = bx, by, ax, ay

        lo, hi = 0, px // ax

        while lo <= hi:
            a = (hi + lo) // 2
            hx, hy = ax * a, ay * a

            b = (py - hy) // by

            if by * (px - hx) > (py - hy) * bx:
                lo = a + 1
            elif by * (px - hx) < (py - hy) * bx:
                hi = a - 1
            else:
                if (px - hx) % bx == 0 and (py - hy) % by == 0:
                    r += (b * 3 + a) if swapped else (a * 3 + b)
                break

    return r


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[tuple[int, int, int, int, int, int]]]:
        foo = []

        pat_a = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
        pat_b = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
        pat_p = re.compile(r"Prize: X=(\d+), Y=(\d+)")

        lines = iter(input.splitlines())

        while True:
            ax, ay = re.match(pat_a, next(lines)).groups()  # type: ignore
            bx, by = re.match(pat_b, next(lines)).groups()  # type: ignore
            px, py = re.match(pat_p, next(lines)).groups()  # type: ignore

            foo.append((int(ax), int(ay), int(bx), int(by), int(px), int(py)))

            try:
                next(lines)
            except StopIteration:
                break

        return (foo,)

    def part_one_impl(self, foo: list[tuple[int, int, int, int, int, int]]) -> int:  # type: ignore
        return solution(foo)

    def part_two_impl(self, foo: list[tuple[int, int, int, int, int, int]]) -> int:  # type: ignore
        D = 10000000000000
        return solution(list(map(lambda t: (t[0], t[1], t[2], t[3], t[4] + D, t[5] + D), foo)))
