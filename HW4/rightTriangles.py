#Problem 3
import sys
import math

n = int(sys.stdin.readline())
points = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

answer = 0

# Check each point as the possible right-angle vertex.
for i in range(n):
    x1, y1 = points[i]
    directions = {}

    # Count the directions from this point to every other point.
    for j in range(n):
        if i == j:
            continue

        dx = points[j][0] - x1
        dy = points[j][1] - y1

        # Reduce the direction to its simplest integer form.
        divisor = math.gcd(abs(dx), abs(dy))
        direction = (dx // divisor, dy // divisor)

        directions[direction] = directions.get(direction, 0) + 1

    # Perpendicular directions form a right angle.
    for dx, dy in directions:
        perpendicular = (-dy, dx)
        answer += directions[(dx, dy)] * directions.get(perpendicular, 0)

print("The number of right triangles is:", answer)
