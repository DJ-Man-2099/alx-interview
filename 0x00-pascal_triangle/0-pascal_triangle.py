#!/usr/bin/python3
# Pascal Triangle

def pascal_triangle(n):
    """Pascal Triangle Calculator"""
    result = []
    if n > 0:
        # The First and last indices of each row are always 1
        # the rest is equal to the previous row's index + the previous row's index - 1
        result.append([1])
        if n > 1:
            for i in range(1, n):
                row = []
                index = 0
                while index <= i:
                    if index == 0 or index == i:
                        row.append(1)
                    else:
                        prev_row = result[i-1]
                        row.append(prev_row[index]+prev_row[index-1])
                    index += 1
                result.append(row)
    return result
