from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[int | None]]:
        arr = []
        for i, char in enumerate(input):
            for _ in range(int(char)):
                arr.append(i // 2 if not i % 2 else None)

        return (arr,)

    def part_one_impl(self, disk: list[int | None]) -> int:  # type: ignore
        disk = disk[:]

        l, r = 0, len(disk) - 1

        while True:
            while disk[l] is not None:
                l += 1

            if l >= r:
                break

            disk[l] = disk[r]
            disk[r] = None

            while disk[r] is None:
                r -= 1

        return sum([i * n for i, n in enumerate(disk[:l])])

    def part_two_impl(self, disk: list[int | None]) -> int:  # type: ignore
        disk = disk[:]

        last_id = None

        i = len(disk) - 1
        while i > 0:
            while disk[i] is None:
                i -= 1

            id = disk[i]

            n = 0
            while disk[i] == id:
                i -= 1
                n += 1

            if last_id is None:
                last_id = id

            if last_id < id:
                continue

            last_id = id

            j = leftmost_span(disk[: i + 1], n)

            if j is None:
                continue

            for k in range(n):
                disk[j + k] = disk[i + 1 + k]
                disk[i + 1 + k] = None

        return sum([i * n for i, n in enumerate(disk) if n is not None])


def leftmost_span(disk: list[int | None], n: int) -> int | None:
    l = r = 0

    while True:
        while r < len(disk) and disk[r] is not None:
            r += 1

        l = r

        while r < len(disk) and disk[r] is None:
            r += 1

        if r - l >= n:
            return l

        if r >= len(disk):
            return None


def disk_to_string(disk):
    foo = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    string = ""
    for x in disk:
        string += foo[x % len(foo)] if x is not None else "."
    return string
