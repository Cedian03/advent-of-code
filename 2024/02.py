from advent import BaseSolution


class Solution(BaseSolution):
    def part_one(self) -> int:
        res = 0

        for report in self.input.splitlines():
            d = 0

            levels = list(map(int, report.split()))

            for a, b in zip(levels, levels[1:]):
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

    def part_two(self) -> int:
        safe = 0

        for report in self.input.splitlines():
            levels = list(map(int, report.split()))

            for i in range(len(levels)):
                clone = levels[:i] + levels[i + 1 :]

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
