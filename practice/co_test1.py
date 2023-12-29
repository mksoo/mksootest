import sys

input = sys.stdin.readline

text = input().rstrip()

text = 'Mississipi'

result = {}

for t in text:
    t = t.upper()
    if t not in result:
        result[t] = 1
    else:
        result[t] += 1

max_num = 0
max_char = ''
for char in result:
    num = result[char]

    if max_num < num:
        max_char = char
        max_num = num
    elif max_num == num:
        max_char = '?'

print(max_char)