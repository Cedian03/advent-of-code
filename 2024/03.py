from advent import BaseSolution

import re


class Solution(BaseSolution):
    def part_one(self) -> int:
        return sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", self.input)])

    def part_two(self) -> int:
        sum = 0
        do = True

        for string in map(lambda i: self.input[i:], range(len(self.input))):
            if do and (mat := re.match(r"mul\((\d+),(\d+)\)", string)):
                x, y = mat.groups()
                sum += int(x) * int(y)
            elif string.startswith("do()"):
                do = True
            elif string.startswith("don't()"):
                do = False

        return sum
