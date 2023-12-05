import math
from multiprocessing import Pool

with open("first.data", "r") as f:
    lines = f.read()

blocks = lines.split("\n\n")

class Mapping:
    def __init__(self, from_range_start, to_range_start, length):
        self.lower = int(from_range_start)
        self.upper = self.lower + int(length) - 1
        self.to_offset = int(to_range_start) - self.lower

seeds, lines = blocks[0], blocks[1:]
seeds = list(map(int, seeds.split(":")[1].split()))
mappings_list = []  # [[Mapping1, Mapping2, ...], [Mapping5, Mapping6, ...]]
for line in lines:
    values = map(str.split, line.splitlines()[1:])
    tmp = []
    for to_range_start, from_range_start, length in values:
        tmp.append(Mapping(int(from_range_start), int(to_range_start), int(length)))
    mappings_list.append(tmp)

def silver():
    lowest = math.inf
    for seed in seeds:
        value = seed
        for mappings in mappings_list:
            for mapping in mappings:
                if mapping.lower <= value <= mapping.upper:
                    value += mapping.to_offset
                    break
        lowest = min(value, lowest)
    return lowest

print("silver", silver())


def gold(sneeds):
    seed, seed_range = sneeds
    lowest = math.inf
    print("seed", seed, seed_range)
    for i in range(seed_range):
        value = seed + i
        for mappings in mappings_list:
            for mapping in mappings:
                if mapping.lower <= value <= mapping.upper:
                    value += mapping.to_offset
                    break
        lowest = min(value, lowest)
    return lowest

sneeds = zip(seeds[::2], seeds[1::2])
pool = Pool(12)
lowests = pool.map(gold, sneeds)
print("gold", min(lowests))
# $ time pypy3 first.py
# silver 579439039
# gold 7873084
#
# real	8m31.196s
# user	20m4.245s
# sys	0m0.097s

