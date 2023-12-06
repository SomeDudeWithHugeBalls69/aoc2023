import math
import numpy as np

times, records = map(list, map(lambda x: x.split(":")[1].split(), open("data.txt", "r").read().splitlines()))

def solve(time, record):
    lo, hi = sorted(np.roots([-1, time, -record]))
    return math.floor(hi) - math.ceil(lo) + 1

print("silver", math.prod([solve(int(time), int(record)) for time, record in zip(times, records)]))
print("gold", solve(int("".join(times)), int("".join(records))))