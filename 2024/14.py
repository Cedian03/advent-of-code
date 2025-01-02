from advent import BaseSolution

import re
from dataclasses import dataclass

WIDTH = 101
HEIGHT = 103


@dataclass
class Robot:
    x: int
    y: int
    dx: int
    dy: int

    def step(self, n: int = 1):
        self.x = (self.x + self.dx * n) % WIDTH
        self.y = (self.y + self.dy * n) % HEIGHT


def score(robots: list[Robot]):
    q1 = q2 = q3 = q4 = 0

    for robot in robots:
        if robot.x > WIDTH // 2:
            if robot.y > HEIGHT // 2:
                q1 += 1
            elif robot.y < HEIGHT // 2:
                q4 += 1
        elif robot.x < WIDTH // 2:
            if robot.y > HEIGHT // 2:
                q2 += 1
            elif robot.y < HEIGHT // 2:
                q3 += 1

    return q1 * q2 * q3 * q4


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[Robot]]:
        return (
            [
                Robot(*map(int, re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line).groups()))
                for line in input.splitlines()
            ],
        )

    def part_one_impl(self, robots: list[Robot]) -> int:  # type: ignore
        robots = robots[:]

        for robot in robots:
            robot.step(100)

        return score(robots)

    def part_two_impl(self, robots: list[Robot]) -> int:  # type: ignore
        robots = robots[:]

        i = 0
        while True:
            mat = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

            for robot in robots:
                robot.step()

                mat[robot.y][robot.x] = True
            i += 1

            for row in mat:
                if sum(row) >= 30:
                    xprint(mat)
                    print(f"^^ After {i} seconds\n")
                    input("")
                    break


def xprint(mat):
    for row in mat:
        print("".join(map(lambda b: "#" if b else ".", row)))
