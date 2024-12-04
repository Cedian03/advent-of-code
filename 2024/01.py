from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[int], list[int]]:
        left: list[int] = []
        right: list[int] = []

        for line in input.splitlines():
            x, y = line.split()
            left.append(int(x))
            right.append(int(y))

        return left, right

    def part_one_impl(self, left: list[int], right: list[int]) -> int:  # type: ignore
        return sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])

    def part_two_impl(self, left: list[int], right: list[int]) -> int:  # type: ignore
        return sum([x * right.count(x) for x in left])
