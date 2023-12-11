from collections import defaultdict
from queue import Queue

with open("data.txt", "r") as f:
    lines = f.read().splitlines()


class Node():
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char
        self.neighbors = []
        self.distance = -1

    def debug_info(self):
        return self.x, self.y, self.char, self.neighbors, self.distance

    def __repr__(self):
        return str(self.char)


NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

# populate field with nodes
field = defaultdict(lambda: Node(None, None, None))
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        field[(x, y)] = Node(x, y, char)


# returns: neighbor_offset1, neighbor_offset2
def parse_char(char):
    if char == "|":
        return NORTH, SOUTH
    elif char == "-":
        return EAST, WEST
    elif char == "L":
        return NORTH, EAST
    elif char == "J":
        return NORTH, WEST
    elif char == "7":
        return SOUTH, WEST
    elif char == "F":
        return SOUTH, EAST


# connect nodes
start = None
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = field[(x, y)]
        elif char != ".":
            neighbor1, neighbor2 = parse_char(char)  # TODO: improve naming
            node = field[(x, y)]
            node.neighbors.append(field[x + neighbor1[0], y + neighbor1[1]])
            node.neighbors.append(field[x + neighbor2[0], y + neighbor2[1]])

# connect start node
for node in field.values():
    if start in node.neighbors:
        start.neighbors.append(node)
start.distance = 0


# calc distances BFS
queue = Queue()
queue.put(start)
while not queue.empty():
    cur = queue.get()
    for neighbor in cur.neighbors:
        if neighbor.distance == -1:
            neighbor.distance = cur.distance + 1
            queue.put(neighbor)

print("silver", max([node.distance for node in field.values()]))



# ---------- gold -------------
# first idea was to double the resolution and then flood fill, to catch the "in between squeezing" part
# but that's just boring and annoying to do and I am lazy...
# Will maybe do later
