class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count_nodes = 0

    def add(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count_nodes += 1
            return

        if value <= self.head.value:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count_nodes += 1
            return

        current = self.head

        while current.next is not None and current.next.value < value:
            current = current.next

        new_node.next = current.next
        new_node.prev = current

        if current.next is not None:
            current.next.prev = new_node
        else:
            self.tail = new_node

        current.next = new_node
        self.count_nodes += 1

    def delete(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                if current.prev is None:
                    self.head = current.next
                else:
                    current.prev.next = current.next

                if current.next is None:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev

                self.count_nodes -= 1
                return True

            current = current.next

        return False

    def exists(self, value):
        def search(node):
            if node is None:
                return False

            if node.value == value:
                return True

            return search(node.next)

        return search(self.head)

    def count(self, value):
        def count_values(node):
            if node is None:
                return 0

            if node.value == value:
                return 1 + count_values(node.next)

            return count_values(node.next)

        return count_values(self.head)

    def print_list(self):
        def print_nodes(node):
            if node is None:
                return

            if node.next is None:
                print(node.value)
            else:
                print(node.value, end=" <-> ")
                print_nodes(node.next)

        if self.head is None:
            print("(empty)")
        else:
            print_nodes(self.head)

    def total(self):
        def add_values(node):
            if node is None:
                return 0

            return node.value + add_values(node.next)

        return add_values(self.head)

    def sum_middle_three(self):
        if self.count_nodes < 3:
            return None

        middle = self.count_nodes // 2
        current = self.head
        if self.count_nodes % 2 == 1:
            for _ in range(middle - 1):
                current = current.next
        else:
            for _ in range(middle - 2):
                current = current.next



        return current.value + current.next.value + current.next.next.value

    def median(self):
        if self.count_nodes == 0:
            return None

        middle = self.count_nodes // 2
        current = self.head

        for _ in range(middle):
            current = current.next

        if self.count_nodes % 2 == 1:
            return current.value

        return (current.prev.value + current.value) / 2