import sys
from problem2 import SinglyLinkedList


my_list = SinglyLinkedList()

line_number = 0

for line in sys.stdin:
    line_number += 1
    line = line.strip()

    if line == "" or line.startswith("#"):
        continue

    parts = line.split()
    command = parts[0]

    try:
        if command == "append":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'append <value>', got '{line}'")
                continue
            my_list.append(int(parts[1]))

        elif command == "prepend":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'prepend <value>', got '{line}'")
                continue
            my_list.prepend(int(parts[1]))

        elif command == "insert":
            if len(parts) != 3:
                print(f"line {line_number}: expected 'insert <index> <value>', got '{line}'")
                continue
            index = int(parts[1])
            value = int(parts[2])
            my_list.insert(index, value)

        elif command == "get":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'get <index>', got '{line}'")
                continue
            index = int(parts[1])
            print(f"get({index}) = {my_list.get(index)}")

        elif command == "find":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'find <value>', got '{line}'")
                continue
            value = int(parts[1])
            print(f"find({value}) = {my_list.find(value)}")

        elif command == "len":
            if len(parts) != 1:
                print(f"line {line_number}: expected 'len', got '{line}'")
                continue
            print(f"len = {len(my_list)}")

        elif command == "update":
            if len(parts) != 3:
                print(f"line {line_number}: expected 'update <index> <value>', got '{line}'")
                continue
            index = int(parts[1])
            value = int(parts[2])
            my_list.update(index, value)

        elif command == "delete":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'delete <value>', got '{line}'")
                continue
            value = int(parts[1])

            if not my_list.delete(value):
                print(f"line {line_number}: {value} not found, nothing deleted")

        elif command == "delete_at":
            if len(parts) != 2:
                print(f"line {line_number}: expected 'delete_at <index>', got '{line}'")
                continue
            index = int(parts[1])
            value = my_list.delete_at(index)
            print(f"delete_at({index}) = {value}")

        elif command == "print_list":
            if len(parts) != 1:
                print(f"line {line_number}: expected 'print_list', got '{line}'")
                continue
            my_list.print_list()

        else:
            print(f"line {line_number}: unknown directive '{command}'")

    except ValueError:
        print(f"line {line_number}: index must be a whole number, got '{line}'")

    except IndexError:
        print(f"line {line_number}: index {index} out of range")


print("Final list:", end=" ")
my_list.print_list()