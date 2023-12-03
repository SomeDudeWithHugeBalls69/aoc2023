from collections import namedtuple

with open("data.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def get_first_num(string):
    for c in string:
        if 48 <= ord(c) <= 57:
            return c

def silver(lines):
    result = 0
    for line in lines:
        left = get_first_num(line)
        right = get_first_num(reversed(line))
        result += int(left + right)
    
    return result

print("silver", silver(lines))  # 54697


string_to_num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
reversed_string_to_num = {key[::-1]: num for key, num in string_to_num.items()}

def gold():
    class Trie:
        def __init__(self, mapping):
            self.root = {}
            for string, num in mapping.items():
                cur = self.root
                for char in string:
                    if char not in cur:
                        cur[char] = {}
                    cur = cur[char]
                cur["end"] = num

        def get(self, string, index):
            cur = self.root
            for i in range(index, len(string)):
                if string[i] not in cur:
                    return None
                cur = cur[string[i]]
                if "end" in cur:
                    return cur["end"]
            return None

    def get_first_num_or_num_string(string, trie):
        for i in range(len(string)):
            if string[i].isdigit():
                return string[i]
            num = trie.get(string, i)
            if num:
                return num

    trie = Trie(string_to_num)
    reversed_trie = Trie(reversed_string_to_num)
    result = 0
    for line in lines:
        left = get_first_num_or_num_string(line, trie)
        right = get_first_num_or_num_string(line[::-1], reversed_trie)
        result += int(left + right)
    return result

print("gold", gold()) # 54885


# $ pypy3 bigboi.py
# silver 55022487 0.149840 sec
# gold 55015199 0.645620 sec
