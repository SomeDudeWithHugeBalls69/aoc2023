from collections import defaultdict

with open("first.data", "r") as f:
    lines = f.read().splitlines()


# --------------- parse ---------------
field = defaultdict(lambda: ".")
for y, line in enumerate(lines):
    for x, symbol in enumerate(line):
        field[(x, y)] = symbol


numbers = {}  # (x, y) -> "123"
for (x, y), symbol in list(field.items()).copy():
    if symbol.isdigit() and not field[(x-1, y)].isdigit():
        offset = 1
        right_symbol = field[(x+offset, y)]
        while right_symbol.isdigit():
            symbol += right_symbol
            offset += 1
            right_symbol = field[(x+offset, y)]
        numbers[(x, y)] = symbol

# --------------- silver ---------------
def has_part_in_neighborhood(number, number_x, number_y):
    for x in range(number_x - 1, number_x + len(number) + 1):
        for y in range(number_y - 1, number_y + 2):
            symbol = field[(x, y)]
            if not symbol.isdigit() and symbol != ".":
                return True
    return False

count = 0
for (number_x, number_y), number in numbers.items():
    if has_part_in_neighborhood(number, number_x, number_y):
        count += int(number)

print("silver", count)

# --------------- gold ---------------
# gears = {}  # {(x, y): [number1, number2,...], ...}
gears = defaultdict(lambda: [])
for (number_x, number_y), number in numbers.items():
    for x in range(number_x - 1, number_x + len(number) + 1):
        for y in range(number_y - 1, number_y + 2):
            if field[(x, y)] == "*":
                gears[(x, y)].append(number)

gold = 0
for numbers in gears.values():
    if len(numbers) == 2:
        gold += int(numbers[0]) * int(numbers[1])

print("gold", gold)  # 84051670
