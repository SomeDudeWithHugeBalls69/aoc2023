import numpy as np

with open("data.txt", "r") as f:
    lines = [list(map(int, line.split())) for line in f.read().splitlines()]



def silver(values):
    history = [values]
    while sum(history[-1]) != 0:
        line = []
        for a, b in zip(history[-1], history[-1][1:]):
            line.append(b - a)
        history.append(line)

    return sum([line[-1] for line in history])

print("silver", sum([silver(line) for line in lines]))

def gold(values):
    history = [values]
    while sum(history[-1]) != 0:
        line = []
        for a, b in zip(history[-1], history[-1][1:]):
            line.append(b - a)
        history.append(line)

    first_row = np.array([line[0] for line in history])
    alternating_sigh = [1, -1] * (len(first_row) // 2 + 1)
    new_row = first_row * alternating_sigh[:len(first_row)]
    return sum(new_row)

print("gold", sum([gold(line) for line in lines]))
