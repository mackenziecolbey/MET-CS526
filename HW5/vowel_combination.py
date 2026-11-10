##homework 5
##vowel combination
#problem 2

import sys

vowels = [".", ".-", "..", "---", "..-"]

filename = sys.argv[1]

with open(filename, "r") as file:
    file.readline()
    code = file.readline().strip()


n = len(code)
dp = [0] * (n + 1)
dp[0] = 1

for j in range(1, n + 1):
    for vowel_code in vowels:
        if j >= len(vowel_code):
            if code[j - len(vowel_code):j] == vowel_code:
                dp[j] += dp[j - len(vowel_code)]

print("File Input:", filename)
print("The Number of Vowel combinations is:", dp[n])
