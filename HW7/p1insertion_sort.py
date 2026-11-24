##problem 1
##insertion sort

import sys


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current_number = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > current_number:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current_number

    return numbers


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

    sorted_numbers = insertion_sort(numbers)

    print("\nSorted values:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
