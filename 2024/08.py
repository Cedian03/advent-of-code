from advent import BaseSolution

from collections import defaultdict


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
        antennas = defaultdict(list)

        lines = input.splitlines()

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char != ".":
                    antennas[char].append((x, y))

        return (dict(antennas), len(lines[0]), len(lines))

    def part_one_impl(self, antennas: dict[str, list[tuple[int, int]]], width: int, height: int) -> int:  # type: ignore
        antinodes = set()

        for _, nodes in antennas.items():
            for i, (ax, ay) in enumerate(nodes):
                for bx, by in nodes[i + 1 :]:
                    dx = bx - ax
                    dy = by - ay

                    for x, y in ((ax - dx, ay - dy), (bx + dx, by + dy)):
                        if x in range(width) and y in range(height):
                            antinodes.add((x, y))

        return len(antinodes)

    def part_two_impl(self, antennas: dict[str, list[tuple[int, int]]], width: int, height: int) -> int:  # type: ignore
        antinodes = set()

        for _, nodes in antennas.items():
            for i, (ax, ay) in enumerate(nodes):
                for bx, by in nodes[i + 1 :]:
                    dx = bx - ax
                    dy = by - ay

                    for (x, y), (dx, dy) in (((ax, ay), (dx, dy)), ((bx, by), (-dx, -dy))):
                        while x in range(width) and y in range(height):
                            antinodes.add((x, y))

                            x += dx
                            y += dy

        return len(antinodes)
