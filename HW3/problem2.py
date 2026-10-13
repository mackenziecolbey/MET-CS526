def find_substrings(text, start, substrings):
    if start == len(text):
        return

    for end in range(start + 1, len(text) + 1):
        substrings.add(text[start:end])

    find_substrings(text, start + 1, substrings)


text = input().strip()
substrings = set()

find_substrings(text, 0, substrings)

for substring in sorted(substrings):
    print(substring)

print(len(substrings))
