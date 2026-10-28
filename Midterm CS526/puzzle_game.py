#Midterm problem 3 - symbol puzzle game
import sys
import math

def solve(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        symbols = file.readline().strip().split(",")

        board = []
        for line in file:
            board.append(line.strip().split(","))

    allowed = set(symbols)
    sub_size = int(math.sqrt(n))

    for row in range(n):
        seen = set()

        for col in range(n):
            value = board[row][col]

            if value == ".":
                continue

            if value not in allowed or value in seen:
                return "The board is invalid"

            seen.add(value)

    for col in range(n):
        seen = set()

        for row in range(n):
            value = board[row][col]

            if value == ".":
                continue

            if value in seen:
                return "The board is invalid"

            seen.add(value)
    for start_row in range(0, n, sub_size):
        for start_col in range(0, n, sub_size):
            seen = set()

            for row in range(start_row, start_row + sub_size):
                for col in range(start_col, start_col + sub_size):
                    value = board[row][col]

                    if value == ".":
                        continue

                    if value in seen:
                        return "The board is invalid"

                    seen.add(value)

    return "The board is valid"

def main():
    filename = sys.argv[1]
    print(solve(filename))

if __name__ == "__main__":
    main()