##probme 1
##merge sort

import sys


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


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

    sorted_numbers = merge_sort(numbers)

    print("\nSorted values:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
