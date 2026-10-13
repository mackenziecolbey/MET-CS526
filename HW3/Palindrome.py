
count = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    line = line.replace(" ", "")

    if line == line[::-1]:
        print("True")
        count = count + 1
    else:
        print("False")

print(count)
