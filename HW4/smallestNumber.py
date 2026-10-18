##Problem 2
import sys

n = int(sys.stdin.readline())
T = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

original_array = array.copy()
array.sort(reverse=True)

total = 0
count = 0

for number in array:
    total += number
    count += 1

    if total > T:
        break

print("Input:", ",".join(map(str, original_array)), "Target:", T, "Answer:", count)

