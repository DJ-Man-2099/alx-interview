#!/usr/bin/python3
"""
Optional Task 1
"""
import sys


class Position():
    """Class for defining Positions"""

    def __init__(self, x, y):
        """Initialize Position in terms of x and y"""
        self.x = x
        self.y = y

    def is_on_same_diagonal(self, other_pos):
        """checks if 2 points on same diagonal"""
        x_difference = self.x - other_pos.x
        y_difference = self.y - other_pos.y
        if x_difference == 0 or y_difference == 0:
            return self.is_on_same_line(other_pos)
        return abs(x_difference/y_difference) == 1

    def is_on_same_line(self, other_pos):
        """checks if 2 points on same line"""
        return self.x == other_pos.x or self.y == other_pos.y

    def __str__(self):
        """String Representation"""
        return f"[{self.x}, {self.y}]"

    def toList(self):
        """to List for testing"""
        return [self.x, self.y]

    def __repr__(self):
        """String Representation"""
        return f"[{self.x}, {self.y}]"


def nqueens(size=""):
    """
    solves the nqueens problem
    """
    if not size.isdigit():
        print("N must be a number")
        sys.exit(1)
    int_size = int(size)
    if int_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    # all_positions = get_all_positions(int_size)
    # print(f"number of solutions: {len(all_positions)}")
    possible_solutions = get_possible_solutions(int_size)
    # possible_solutions = all_positions
    # list_pos_sol = []
    for solution in possible_solutions:
        print(solution)
    #     list_pos_sol.append(list(map(lambda p: p.toList(), solution)))
    # return list_pos_sol


# def get_all_positions(size=0):
#     """
#     returns list of all positions
#     """
#     positions = []
#     for i in range(size):
#         for j in range(size):
#             positions.append(Position(i, j))
#     return positions


def get_possible_solutions(number=0):
    """
    returns list of possible solutions
    """
    # Create all possible solutions
    # valid_solutions = []
    # all_solutions = get_all_combinations(positions, number)
    # for solution in all_solutions:
    #     if check_if_valid_solution(solution):
    #         valid_solutions.append(list(solution))

    # Create solution step by step
    return build_solution(number=number)


def build_solution(number=0, solution=[]):
    """build a solution using backtracking"""
    current_row = len(solution)
    if number == current_row:
        # If we've placed all queens, return the solution
        return [solution]

    solutions = []
    for i in range(number):
        possible_position = Position(current_row, i)
        # Check if this position is safe
        # print(
        # f"Checking position: {possible_position}, for solution: {solution}")
        if all(map(lambda p: is_not_attacking(possible_position, p),
                   solution)):
            # If it's safe, place a queen at this position and recurse
            new_solutions = build_solution(
                number, solution + [possible_position])
            solutions.extend(new_solutions)

    return solutions


# def get_all_combinations(base=[], size=0):
#     """create all possible solutions"""
#     # size is more than no of elements
#     # only one combination
#     base_size = len(base)
#     if size >= base_size:
#         return [base]
#     combinations = []
#     # base case:
#     # len(base) = 2, size = 1
#     if base_size > 1:
#         for i in range(base_size-size+1):
#             if size == 1:
#                 combinations.append(base[i:i+size])
#             else:
#                 rest = base[i+1:]
#                 temp = [base[i]]
#                 for c in get_all_combinations(rest, size - 1):
#                     combinations.append(temp + c)

#     return combinations


def is_not_attacking(pos_1, pos_2):
    """Check if the 2 positions aren't attacking"""
    is_on_line = pos_1.is_on_same_line(pos_2)
    is_on_diagonal = pos_1.is_on_same_diagonal(pos_2)
    # print(f"{pos_1} is on same line as {pos_2}: {is_on_line}")
    # print(f"{pos_1} is on same diagonal as {pos_2}: {is_on_diagonal}")
    if is_on_line or is_on_diagonal:
        return False
    return True


def check_if_valid_solution(
    solution=[]
) -> bool:
    """
    check if solution is valid
    """
    for i in range(len(solution)):
        pos = solution[i]
        if any(map(lambda x: not is_not_attacking(pos, x), solution[i+1:])):
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
    # check_if_valid_solution(valid_solutions[1])
    # print(get_all_combinations([1, 2, 3, 4], 3))
    # sols = build_solution(
    #     list(map(lambda p: Position(p[0], p[1]),
    # [[0, 1], [1, 3], [2, 0], [3, 2], [0, 0]])), 4)
    # if sols:
    #     for s in sols:
    #         print(s)
