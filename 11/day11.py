import itertools
import math
from collections import defaultdict

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

field = [["."] * len(lines) for i in range(len(lines[0]))]
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            field[y][x] = "#"

# expand horizontally
for x in range(len(field[0])-1, -1, -1):
    col_has_galaxy = False
    for y in range(len(field)-1, -1, -1):
        if field[y][x] == "#":
            col_has_galaxy = True
            break
    if not col_has_galaxy:
        for y in range(len(field)):
            field[y].insert(x, ".")

# expand vertically
for y in range(len(field)-1, -1, -1):
    if all([char == "." for char in field[y]]):
        field.insert(y, ["."] * len(field[0]))

# grab galaxies
galaxies = []
for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] == "#":
            galaxies.append((x, y))

# calc each combination
distances = {}
for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    distances[tuple(sorted([galaxy1, galaxy2]))] = abs(x2 - x1) + abs(y2 - y1)


print(sum(distances.values())) # 374

# thought there would be some kind of fun continuous galaxy expansion over time and some other
# distance metric, so I did the array expansion around...

# for gold, just add the expansion factor depending on existance of other galaxy coords that are greater, for each coord
# can't be bothered
