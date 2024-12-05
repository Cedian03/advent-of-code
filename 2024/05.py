from advent import BaseSolution

from functools import cmp_to_key


def is_correct_update(rules: list[tuple[int, int]], update: list[int]) -> bool:
    for i, a in enumerate(update):
        for b in update[i + 1 :]:
            for x, y in rules:
                if x == b and y == a:
                    return False
    return True


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
        lines = iter(input.splitlines())

        rules = []
        for line in lines:
            if not line:
                break

            x, y = map(int, line.split("|"))
            rules.append((x, y))

        updates = []
        for line in lines:
            updates.append(list(map(int, line.split(","))))

        return (rules, updates)

    def part_one_impl(self, rules: list[tuple[int, int]], updates: list[list[int]]) -> int:  # type: ignore
        result = 0

        for update in updates:
            if is_correct_update(rules, update):
                result += update[len(update) // 2]

        return result

    def part_two_impl(self, rules: list[tuple[int, int]], updates: list[list[int]]) -> int:  # type: ignore
        def cmp(a: int, b: int) -> int:
            for x, y in rules:
                if x == a and y == b:
                    return 1
                elif x == b and y == a:
                    return -1
            return 0

        result = 0

        for update in updates:
            if not is_correct_update(rules, update):
                corrected_update = update[:]
                corrected_update.sort(key=cmp_to_key(cmp))

                result += corrected_update[len(corrected_update) // 2]

        return result
