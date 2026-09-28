class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    def insert(self, index, value):
        if index < 0 or index > self.count:
            raise IndexError("index out of range")

        if index == 0:
            self.prepend(value)
            return

        if index == self.count:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def get(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("index out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def find(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index

            current = current.next
            index += 1

        return -1

    def __len__(self):
        return self.count

    def update(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError("index out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        current.value = value

    def delete(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self.count -= 1

            if self.count == 0:
                self.tail = None

            return True

        current = self.head

        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current

                current.next = current.next.next
                self.count -= 1
                return True

            current = current.next

        return False

    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("index out of range")

        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self.count -= 1

            if self.count == 0:
                self.tail = None

            return value

        current = self.head

        for _ in range(index - 1):
            current = current.next

        value = current.next.value

        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        self.count -= 1

        return value

    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        current = self.head
        values = []

        while current is not None:
            values.append(str(current.value))
            current = current.next

        print(" -> ".join(values))