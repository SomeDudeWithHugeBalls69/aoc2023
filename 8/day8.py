import time
from collections import namedtuple
import numpy as np

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

instructions, lines = lines[0], lines[2:]
Node = namedtuple("Node", ["name", "left", "right"])
nodes = {line[:3]: Node(line[:3], line[7:10], line[12:15]) for line in lines}


cur = nodes["AAA"]
i = 0
while True:
    direction = instructions[i % len(instructions)]
    if direction == "R":
        cur = nodes[cur.right]
    else:
        cur = nodes[cur.left]
    i += 1
    if cur == nodes["ZZZ"]:
        break

print("silver", i)


def cycle_length(start_node):
    cur = start_node
    i = 0
    while True:
        direction = instructions[i % len(instructions)]
        if direction == "R":
            cur = nodes[cur.right]
        else:
            cur = nodes[cur.left]
        i += 1
        if cur.name.endswith("Z"):
            break
    return i

start_nodes = [node for name, node in nodes.items() if name.endswith("A")]
cycle_lengths = [cycle_length(start_node) for start_node in start_nodes]
print("gold", np.lcm.reduce(cycle_lengths))
