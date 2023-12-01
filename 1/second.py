from collections import namedtuple

with open("first.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def get_first_num(string):
    for c in string:
        if 48 <= ord(c) <= 57:
            return c

def silver(lines):
    sum = 0
    for line in lines:
        left = get_first_num(line)
        right = get_first_num(reversed(line))
        sum += int(left + right)
    
    return sum

print("silver", silver(lines))  # 54697


string_to_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# brute forcing or string replacements are boring :)

def gold_cool_kids(lines):
    # Implemented without looking anything up:
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

        def get(self, string):
            cur = self.root
            for char in string:
                if char not in cur:
                    return None
                cur = cur[char]
                if "end" in cur:
                    return cur["end"]

            return None

    def get_first_num_or_num_string(string, trie):
        for i in range(len(string)):
            if 48 <= ord(string[i]) <= 57:
                return string[i]
            num = trie.get(string[i:i + longest_word_length])
            if num:
                return num


    trie = Trie(string_to_num)
    reversed_string_to_num = {key[::-1]: num for key, num in string_to_num.items()}
    reversed_trie = Trie(reversed_string_to_num)
    longest_word_length = max([len(key) for key in string_to_num.keys()])

    sum = 0
    for line in lines:
        left = get_first_num_or_num_string(line, trie)
        right = get_first_num_or_num_string(line[::-1], reversed_trie)
        sum += int(left + right)
    
    return sum

print("gold", gold_cool_kids(lines))  # 54885




# after finished, I checked if the naive solution would have worked
# it does not! because of examples like
# cool simple line
# 25 85 deightwoeighteight5
# 21 81 lteightwo2132seven7oneone
# 19 29 jgtwonetwosixthreervlmxlnine869lbqzxpqqn
# 29 89 djdeightwoeightc2six6nine

def gold_simple(lines):
    translated_lines = []
    for line in lines:
        l = line
        for string, num in string_to_num.items():
            l = l.replace(string, num)
        translated_lines.append(l)
    return silver(translated_lines)


for line in lines:
    simple = gold_simple([line])
    cool = gold_cool_kids([line])
    if simple != cool:
        print(simple, cool, line)