
string = "abcdefghijklmnopqrstuvwxyz" * 10
rows = 10
max_chars = 1
current_char = 0

for i in range(rows):
    line = string[current_char:current_char + max_chars]
    print(line.center(rows * 2))
    current_char += max_chars
    max_chars += 2