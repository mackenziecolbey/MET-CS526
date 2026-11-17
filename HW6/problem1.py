##homework 6 problem 1 Merge
import ast
import sys


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, item):
        self.heap.append(item)

        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent], self.heap[index]
                )
                index = parent
            else:
                break

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")

        smallest = self.heap[0]
        last = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last
            index = 0

            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                smallest_child = index

                if (left < len(self.heap) and
                        self.heap[left] < self.heap[smallest_child]):
                    smallest_child = left

                if (right < len(self.heap) and
                        self.heap[right] < self.heap[smallest_child]):
                    smallest_child = right

                if smallest_child != index:
                    self.heap[index], self.heap[smallest_child] = (
                        self.heap[smallest_child], self.heap[index]
                    )
                    index = smallest_child
                else:
                    break

        return smallest


def merge_logs(logs):
    pq = PriorityQueue()
    result = []

    for i in range(len(logs)):
        if len(logs[i]) > 0:
            pq.insert((logs[i][0], i + 1, 0))

    while not pq.is_empty():
        time, register, index = pq.extract_min()

        result.append((time, register))

        next_index = index + 1

        if next_index < len(logs[register - 1]):
            next_time = logs[register - 1][next_index]

            pq.insert((next_time, register, next_index))

    return result


logs = []

for line in sys.stdin:
    if line.strip():
        logs.append(ast.literal_eval(line.strip()))

print(merge_logs(logs))

