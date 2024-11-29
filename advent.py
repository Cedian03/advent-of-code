from argparse import ArgumentParser
from datetime import date
from importlib import import_module
from types import ModuleType
from typing import Callable, Optional


class BaseSolution:
    input: str

    def __init__(self, input: str):
        self.input = input

    def part_one(self) -> int:
        raise NotImplementedError("Part one yet to be implemented")

    def part_two(self) -> int:
        raise NotImplementedError("Part two yet to be implemented")


def get_parser() -> ArgumentParser:
    parser = ArgumentParser("advent")

    today = date.today()
    parser.add_argument("-y", "--year", type=int, default=today.year)
    parser.add_argument("-d", "--day", type=int, default=today.day)

    return parser


def if_implemented(func: Callable[[], int]) -> Optional[int]:
    try:
        return func()
    except NotImplementedError:
        return None


def main():
    args = get_parser().parse_args()

    assert args.day in range(1, 26)

    year: int = args.year
    day: int = args.day

    module_name = f"{year}.{day:02}"
    module_path = f"./{year}/{day:02}.py"
    input_path = f"./{year}/input/{day:02}.dat"

    module: ModuleType
    input: str = ""

    try:
        module = import_module(module_name)
    except ModuleNotFoundError:
        print(f"[ERR] Could not find solution module [{module_path}]")

        with open(module_path, "x") as f, open("./template.py", "r") as g:
            f.write(g.read())

        module = import_module(module_name)

    try:
        with open(input_path, "r") as f:
            input = f.read()
    except FileNotFoundError:
        print(f"[ERR] Could not find puzzle input [{input_path}]")

        with open(input_path, "x") as f:
            pass

    if len(input) <= 20:
        print("[WRN] Puzzle input is very small")

    solution: BaseSolution = module.Solution(input)

    print("1:", if_implemented(solution.part_one) or "Not yet implemented")
    print("2:", if_implemented(solution.part_two) or "Not yet implemented")


if __name__ == "__main__":
    main()
