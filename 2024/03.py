from advent import BaseSolution

import re


class Solution(BaseSolution):
    def part_one_impl(self, input: str) -> int:  # type: ignore
        return sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", input)])

    def part_two_impl(self, input: str) -> int:  # type: ignore
        sum = 0
        do = True

        for string in map(lambda i: input[i:], range(len(input))):
            if do and (mat := re.match(r"mul\((\d+),(\d+)\)", string)):
                x, y = mat.groups()
                sum += int(x) * int(y)
            elif string.startswith("do()"):
                do = True
            elif string.startswith("don't()"):
                do = False

        return sum
