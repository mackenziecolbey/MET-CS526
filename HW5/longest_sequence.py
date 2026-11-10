##homework 5
##longest sequence
##problem 3


import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    data = list(map(int, file.read().split()))

n = data[0]
m = data[1]

A = data[2:2 + n]
B = data[2 + n:2 + n + m]

dp_a = [1] * n
dp_b = [1] * m

for i in range(max(n, m)):

    if i < n:
        for j in range(min(i, m)):
            if B[j] < A[i]:
                dp_a[i] = max(dp_a[i], dp_b[j] + 1)

    if i < m:
        for j in range(min(i, n)):
            if A[j] < B[i]:
                dp_b[i] = max(dp_b[i], dp_a[j] + 1)

longest = max(dp_a + dp_b)

print("File Input:", filename)
print("Longest Sequence:", longest)





