import functools

with open("input.data", "r") as f:
    lines = f.read().splitlines()

# remove "Card "
lines = [line[5:] for line in lines]

### parse
data = {}  # {"1": (set(), set())} # first tuple are winning numbers, second ours
for line in lines:
    id, rest = line.split(":")
    winning_nums, our_nums = map(lambda x: x.split(), rest.split("|"))
    data[int(id)] = (set(winning_nums), set(our_nums))

### silver
def silver():
    points = 0
    for id, (winning_nums, our_nums) in data.items():
        intersection = our_nums & winning_nums
        if len(intersection) > 0:
            points += 2**(len(intersection)-1)
    return points

print("silver", silver())

### gold
@functools.lru_cache(maxsize=None)
def process_scratchcard(id):
    winning_nums, our_nums = data[id]
    intersection = our_nums & winning_nums
    if len(intersection) > 0:
        scratchcard_count = 1
        for i in range(id+1, id+len(intersection)+1):
            if i in data:
                scratchcard_count += process_scratchcard(i)
        return scratchcard_count
    else:
        return 1

count = 0
for id in data:
    count += process_scratchcard(id)

print("gold", count)