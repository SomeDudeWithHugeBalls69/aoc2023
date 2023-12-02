# with open("example.data", "r") as f:
with open("first.data", "r") as f:
    lines = [line.strip() for line in f.readlines()]

lines = [line[5:] for line in lines]

# advent of parse....
data = {}  # {"1": [{"blue": 3, "red": 4}, {"red": 6, ...], "2": ...}
for line in lines:
    game_id, rest = line.split(":")
    game_id = int(game_id)
    data[game_id] = []
    draws = rest.split(";")
    for draw in draws:
        draw = [g.strip() for g in draw.strip().split(",")]
        draw_info = {}
        for color in draw:
            count, color = color.split(" ")
            draw_info[color] = int(count)
        data[game_id].append(draw_info)


max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def is_possible(game):
    for draw in game:
        for color, count in max_cubes.items():
            if color in draw and draw[color] > count:
                return False
    return True


count = 0
for game_id, game in data.items():
    if is_possible(game):
        count += game_id


print("silver", count)

power = 0
for game_id, game in data.items():
    colors = {"blue": 0, "green": 0, "red": 0}
    for draw in game:
        for color, count in draw.items():
            colors[color] = max(colors[color], count)

    power += colors["blue"] * colors["green"] * colors["red"]

print("gold", power)