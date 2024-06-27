#!usr/bin/python3
""" ISLAND PERIMETER """


def island_perimeter(grid):
    """ ISLAND PERIMETER """
    perimeter = 0

    for row in range(len(grid)):
        for elem in range(len(grid[row])):
            if grid[row][elem] == 1:
                perimeter += 4
                if grid[row - 1][elem] == 1 and row > 0:
                    perimeter -= 2
                elif grid[row][elem - 1] == 1 and elem > 0:
                    perimeter -= 2
    return perimeter
