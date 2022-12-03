from aocd.models import Puzzle
import string

puzzle = Puzzle(year=2022, day=3)

data = puzzle.input_data

test = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
values = [i + 1 for i in list(range(52))]

value_dict = {}

for i in range(52):
    value_dict[letters[i]] = values[i]

content = data.split("\n")

points = []

for bag in content:
    split = int(len(bag)/2)
    pocket1, pocket2 = set(bag[:split]), set(bag[split:])
    match = pocket1 & pocket2
    points.append(value_dict[list(match)[0]])

answer_part_1 = sum(points)

print(answer_part_1)

grouped_bags = list(zip(*[iter(content)] * 3))

points2 = []

for bag in grouped_bags:
    elf1, elf2, elf3 = set(bag[0]), set(bag[1]), set(bag[2])
    match = elf1 & elf2 & elf3
    points2.append(value_dict[list(match)[0]])

answer_part_2 = sum(points2)

print(answer_part_2)