import sys
from problem4 import SortedDoublyLinkedList


my_list = SortedDoublyLinkedList()

line_number = 0

for line in sys.stdin:
    line_number += 1
    line = line.strip()

    if line == "" or line.startswith("#"):
        continue

    parts = line.split()
    command = parts[0].lower()

    try:
        if command == "add":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'add <value>', got '{line}'")
                continue

            value = float(parts[1])

            if value.is_integer():
                value = int(value)

            my_list.add(value)
            print(f"add({value})")

        elif command == "delete":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'delete <value>', got '{line}'")
                continue

            value = float(parts[1])

            if value.is_integer():
                value = int(value)

            if my_list.delete(value):
                print(f"delete({value})")
            else:
                print(f"line {line_number}: {value} not found, nothing deleted")

        elif command == "exists":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'exists <value>', got '{line}'")
                continue

            value = float(parts[1])

            if value.is_integer():
                value = int(value)

            print(f"exists({value}) = {my_list.exists(value)}")

        elif command == "count":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'count <value>', got '{line}'")
                continue

            value = float(parts[1])

            if value.is_integer():
                value = int(value)

            print(f"count({value}) = {my_list.count(value)}")

        elif command == "total":
            if len(parts) != 1:
                print(f"line {line_number}: expected 'total', got '{line}'")
                continue

            print(f"total = {my_list.total()}")

        elif command == "sum_middle_three":
            if len(parts) != 1:
                print(f"line {line_number}: expected 'sum_middle_three', got '{line}'")
                continue

            result = my_list.sum_middle_three()

            if result is None:
                print(f"line {line_number}: sum_middle_three needs at least 3 nodes")
            else:
                print(f"sum_middle_three = {result}")

        elif command == "median":
            if len(parts) != 1:
                print(f"line {line_number}: expected 'median', got '{line}'")
                continue

            result = my_list.median()

            if result is None:
                print(f"line {line_number}: median of an empty list")
            else:
                print(f"median = {result}")

        elif command == "print_list":
            if len(parts) != 1:
                print(f"line {line_number}: expected 'print_list', got '{line}'")
                continue

            my_list.print_list()

        else:
            print(f"line {line_number}: unknown directive '{command}'")

    except ValueError:
        print(f"line {line_number}: value must be a number, got '{line}'")


print("Final list:", end=" ")
my_list.print_list()