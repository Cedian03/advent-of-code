from advent import BaseSolution


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[list[list[int]]]:
        return ([[int(x) for x in line.split()] for line in input.splitlines()],)

    def part_one_impl(self, reports: list[list[int]]) -> int:  # type: ignore
        res = 0

        for report in reports:
            d = 0

            for a, b in zip(report, report[1:]):
                if abs(b - a) > 3:
                    break

                match d:
                    case 0:
                        if b > a:
                            d = 1
                        elif b < a:
                            d = -1
                        else:
                            break
                    case 1:
                        if b <= a:
                            break
                    case -1:
                        if b >= a:
                            break
            else:
                res += 1

        return res

    def part_two_impl(self, reports: list[list[int]]) -> int:  # type: ignore
        safe = 0

        for report in reports:
            for i in range(len(report)):
                clone = report[:i] + report[i + 1 :]

                d = 0

                for a, b in zip(clone, clone[1:]):
                    if abs(b - a) > 3:
                        break

                    match d:
                        case 0:
                            if b > a:
                                d = 1
                            elif b < a:
                                d = -1
                            else:
                                break
                        case 1:
                            if b <= a:
                                break
                        case -1:
                            if b >= a:
                                break
                else:
                    safe += 1
                    break

        return safe
