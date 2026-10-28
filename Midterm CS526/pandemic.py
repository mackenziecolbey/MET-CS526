#midterm problem 2 - pandemic

import sys

def solve(filename):
    with open(filename) as file:
        n = int(file.readline())
        grid = [[False for _ in range(n)] for _ in range(n)]

        for line in file:
            row, col = map(int, line.split())
            grid[row][col] = True

    while True:
        new_grid = [row[:] for row in grid]
        new_infections = 0

        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    continue

                infected_neighbors = 0

                if row > 0 and grid[row - 1][col]:
                    infected_neighbors += 1
                if row < n -1 and grid[row + 1][col]:
                    infected_neighbors += 1
                if col > 0 and grid[row][col - 1]:
                    infected_neighbors += 1
                if col < n - 1 and grid[row][col + 1]:
                    infected_neighbors += 1

                if infected_neighbors >= 2:
                    new_grid[row][col] = True
                    new_infections += 1

        grid = new_grid

        if new_infections == 0:
            break

    for row in grid:
        if False in row:
            return "There are healthy counties left"
    return "There are no healthy counties left"

def main():
    filename = sys.argv[1]
    print(solve(filename))

if __name__ == "__main__":
    main()