from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[list[str]], int, int]:
        return (grid := [[x for x in line] for line in input.splitlines()], len(grid), len(grid[0]))

    def part_one_impl(self, grid: list[list[str]], height: int, width: int) -> int:  # type: ignore
        xmases = 0

        for y in range(height):
            for x in range(width):
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        if dy == 0 and dx == 0:
                            continue

                        if ((x + dx * 3) not in range(width)) or ((y + dy * 3) not in range(height)):
                            continue

                        ny = y
                        nx = x

                        for c in "XMAS":
                            if grid[ny][nx] != c:
                                break

                            ny += dy
                            nx += dx
                        else:
                            xmases += 1
        return xmases

    def part_two_impl(self, grid: list[list[str]], height: int, width: int) -> int:  # type: ignore
        xmases = 0

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                if grid[y][x] != "A":
                    continue

                tl = grid[y - 1][x - 1]
                tr = grid[y - 1][x + 1]
                bl = grid[y + 1][x - 1]
                br = grid[y + 1][x + 1]

                if ((tl == "M" and br == "S") or (tl == "S" and br == "M")) and (
                    (tr == "M" and bl == "S") or (tr == "S" and bl == "M")
                ):
                    xmases += 1

        return xmases
