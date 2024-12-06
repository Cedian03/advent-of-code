from advent import BaseSolution

from copy import deepcopy

Map = list[list[bool]]


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[Map, int, int, int, int]:
        map = []
        sx = None
        sy = None
        for y, line in enumerate(input.splitlines()):
            row = []
            for x, char in enumerate(line):
                if char == "^":
                    sx = x
                    sy = y
                row.append(char == "#")
            map.append(row)

        assert sx is not None
        assert sy is not None

        return (map, len(map[0]), len(map), sx, sy)

    def part_one_impl(self, map: Map, width: int, height: int, sx: int, sy: int) -> int:  # type: ignore
        x = sx
        y = sx
        dx = 0
        dy = -1

        visited = {(x, y)}

        while (x + dx) in range(width) and (y + dy) in range(height):
            if map[y + dy][x + dx]:
                dx, dy = -dy, dx
                continue

            x += dx
            y += dy

            visited.add((x, y))

        return len(visited)

    def part_two_impl(self, map: Map, width: int, height: int, sx: int, sy: int) -> int:  # type: ignore
        def is_looping(new_map: Map, x: int, y: int) -> bool:
            dx = 0
            dy = -1

            visited = {((x, y), (dx, dy))}

            while (x + dx) in range(width) and (y + dy) in range(height):
                if new_map[y + dy][x + dx]:
                    dx, dy = -dy, dx
                    continue

                x += dx
                y += dy

                if ((x, y), (dx, dy)) in visited:
                    return True

                visited.add(((x, y), (dx, dy)))
            return False

        looping = 0

        for oy in range(height):
            for ox in range(width):
                if ox == sx and oy == sy:
                    continue

                new_map = deepcopy(map)
                new_map[oy][ox] = True

                looping += is_looping(new_map, sx, sy)

        return looping
