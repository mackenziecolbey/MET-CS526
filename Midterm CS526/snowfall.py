##midterm problem 1 - snowfall

import sys

def solve(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        A = list(map(int, file.readline().split()))

    if n < 3:
        return " ".join(nap(str, A)) + " solution: NO"

    total = A[-1]

    for i in range(n - 2):
        if i == 0:
            window = A[i + 2]
        else:
            window = A[i + 2] - A[i - 1]

        if window * 2 > total:
            return " ".join(map(str, A)) + " solution: YES"

    return " ".join(map(str, A)) + " solution: NO"

def main():
    filename = sys.argv[1]
    print(solve(filename))

if __name__ == "__main__":
    main()