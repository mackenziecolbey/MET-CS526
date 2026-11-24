##problem 1
##quick sort

import sys


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]

    smaller = []
    larger = []

    for number in numbers[:-1]:
        if number <= pivot:
            smaller.append(number)
        else:
            larger.append(number)

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


def main():
    if len(sys.argv) != 2:
        print("Error: Please provide an input filename.")
        return

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip()]

    except (OSError, ValueError):
        print("Error: Could not read the input file or it contains invalid integers.")
        return

    print("Original values:")
    print(numbers)

    sorted_numbers = quick_sort(numbers)

    print("\nSorted values:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
