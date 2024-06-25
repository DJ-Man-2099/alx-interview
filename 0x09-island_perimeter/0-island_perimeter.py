#!/usr/bin/python3
""" Island Perimeter Module """


def get_perim_single(grid, x, y):
    """ checks surroundings """
    edges = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]
    perimeter = 4
    for edge_x, edge_y in edges:
        limit_x = len(grid)
        limit_y = len(grid[x])
        current_x = x+edge_x
        current_y = y+edge_y
        x_within_limit = current_x >= 0 and current_x < limit_x
        y_within_limit = current_y >= 0 and current_y < limit_y
        if (x_within_limit and y_within_limit
                and grid[current_x][current_y] == 1):
            perimeter -= 1

    return perimeter


def island_perimeter(grid):
    """ gets whole param """
    perimeter = 0

    len_x = len(grid)

    for x in range(len_x):
        len_y = len(grid[x])
        for y in range(len_y):
            if grid[x][y] == 1:
                perimeter += get_perim_single(grid, x, y)

    return perimeter
