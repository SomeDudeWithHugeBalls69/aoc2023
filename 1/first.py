with open("data.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def get_first_num(string):
    for c in string:
        if 48 <= ord(c) <= 57:
            return c
        # if c.isdigit():
        # return c

sum = 0
for line in lines:
    left = get_first_num(line)
    right = get_first_num(reversed(line))
    sum += int(left + right)

print("silver", sum)