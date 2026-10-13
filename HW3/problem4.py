#whether any two proton streams cross


def cross(b1, g1, b2, g2):
    x1, y1 = b1
    x2, y2 = g1
    x3, y3 = b2
    x4, y4 = g2

    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    direction = dx1 * dy2 - dy1 * dx2

    if direction != 0:
        return True

    position = (x3 - x1) * dy1 - (y3 - y1) * dx1

    return position == 0


n = int(input())
streams = []

for i in range(n):
    parts = input().split()

    bx = int(parts[1])
    by = int(parts[2])
    gx = int(parts[4])
    gy = int(parts[5])

    streams.append(((bx, by), (gx, gy)))

eliminated = True

for i in range(n):
    for j in range(i + 1, n):
        b1, g1 = streams[i]
        b2, g2 = streams[j]

        if cross(b1, g1, b2, g2):
            eliminated = False

if eliminated:
    print("All Ghosts: were eliminated")
else:
    print("All Ghosts: were not eliminated")
