from dataclasses import dataclass
from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


@dataclass
class Grid:
    color: Color
    visited: bool = False


def max_connected_color(matrix: List[List[Grid]]) -> int:
    max_count = 0

    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            if matrix[i][j].visited is False:
                max_count = max(max_count, traverse(matrix, i, j))

    return max_count


def traverse(matrix: List[List[Grid]], i: int, j: int) -> int:
    matrix[i][j].visited = True

    count = 0

    if check_boundary(matrix, i + 1, j) is True:
        if matrix[i + 1][j].visited is False:
            if matrix[i + 1][j].color == matrix[i][j].color:
                count += traverse(matrix, i + 1, j)

    if check_boundary(matrix, i - 1, j) is True:
        if matrix[i - 1][j].visited is False:
            if matrix[i - 1][j].color == matrix[i][j].color:
                count += traverse(matrix, i - 1, j)

    if check_boundary(matrix, i, j + 1) is True:
        if matrix[i][j + 1].visited is False:
            if matrix[i][j + 1].color == matrix[i][j].color:
                count += traverse(matrix, i, j + 1)

    if check_boundary(matrix, i, j - 1) is True:
        if matrix[i][j - 1].visited is False:
            if matrix[i][j - 1].color == matrix[i][j].color:
                count += traverse(matrix, i, j - 1)

    return count + 1


def check_boundary(matrix: List[List[Grid]], row: int, col: int) -> bool:
    return 0 < row < len(matrix) and 0 < col < len(matrix[0])


matrix = [
    [Grid(Color.GREEN),
     Grid(Color.GREEN),
     Grid(Color.BLUE),
     Grid(Color.RED)],
    [Grid(Color.GREEN),
     Grid(Color.BLUE),
     Grid(Color.RED),
     Grid(Color.BLUE)],
    [Grid(Color.RED),
     Grid(Color.BLUE),
     Grid(Color.BLUE),
     Grid(Color.BLUE)]
]

print(max_connected_color(matrix))
