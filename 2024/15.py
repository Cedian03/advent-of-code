from typing import Any
from advent import BaseSolution

from enum import StrEnum


class Move(StrEnum):
    Up = "^"
    Down = "v"
    Left = "<"
    Right = ">"


class Solution(BaseSolution):
    def parse(self, input: str) -> tuple[Any, ...]:
        lines = iter(input.splitlines())

        x = y = None

        mat = []
        for i, line in enumerate(lines):
            if not line:
                break

            row = []

            for j, char in enumerate(line):
                if char == "@":
                    x, y = j, i
                    row.append(".")
                    continue

                row.append(char)

            mat.append(row)

        moves = []

        for line in lines:
            for move in line:
                moves.append(Move(move))

        return (mat, x, y, moves)

    def part_one_impl(self, mat, x, y, moves) -> int:  # type: ignore
        for move in moves:
            match move:
                case Move.Up:
                    x, y = try_move(mat, x, y, 0, -1)
                case Move.Down:
                    x, y = try_move(mat, x, y, 0, 1)
                case Move.Left:
                    x, y = try_move(mat, x, y, -1, 0)
                case Move.Right:
                    x, y = try_move(mat, x, y, 1, 0)

        return score(mat)

    def part_two_impl(self, mat, x, y, moves) -> int:  # type: ignore
        new_mat = []
        for row in mat:
            new_row = []

            for char in row:
                new_row.append(char)
                new_row.append(char)

            new_mat.append(new_row)

        x *= 2

        for move in moves:
            match move:
                case Move.Up:
                    x, y = try_move(new_mat, x, y, 0, -1)
                case Move.Down:
                    x, y = try_move(new_mat, x, y, 0, 1)
                case Move.Left:
                    x, y = try_move(new_mat, x, y, -1, 0)
                case Move.Right:
                    x, y = try_move(new_mat, x, y, 1, 0)
            print(new_mat)

        return score(mat)


def try_move(mat, x, y, dx, dy) -> tuple[int, int]:
    nx, ny = tx, ty = x + dx, y + dy

    while mat[ny][nx] != "#":
        if mat[ny][nx] == ".":
            mat[ny][nx] = mat[ty][tx]
            mat[ty][tx] = "."

            return tx, ty

        nx += dx
        ny += dy

    return x, y


def score(mat) -> int:
    r = 0

    for y, row in enumerate(mat):
        for x, char in enumerate(row):
            if char == "O":
                r += y * 100 + x

    return r


def xprint(mat, x, y):
    for ry, row in enumerate(mat):
        for rx, char in enumerate(row):
            if rx == x and ry == y:
                assert char == "."
                print("@", end="")
            else:
                print(char, end="")
        print()
